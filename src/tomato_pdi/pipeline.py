from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

import cv2
import numpy as np
from numpy.typing import NDArray

Image = NDArray[np.uint8]
Mask = NDArray[np.uint8]

CLASSES = (
    "Tomato___healthy",
    "Tomato___Late_blight",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
)
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png"}


@dataclass(frozen=True)
class Segmentation:
    raw: Mask
    opened_closed: Mask
    proxy_reference: Mask


def natural_key(path: Path) -> tuple[object, ...]:
    return tuple(
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", path.name)
    )


def discover_images(dataset_dir: Path, samples_per_class: int) -> list[tuple[str, Path]]:
    if samples_per_class < 1:
        raise ValueError("samples_per_class deve ser pelo menos 1.")

    selected: list[tuple[str, Path]] = []
    for label in CLASSES:
        class_dir = dataset_dir / label
        if not class_dir.is_dir():
            raise FileNotFoundError(f"Diretório da classe não encontrado: {class_dir}")
        images = sorted(
            (path for path in class_dir.iterdir() if path.suffix.lower() in IMAGE_SUFFIXES),
            key=natural_key,
        )
        if not images:
            raise FileNotFoundError(f"Nenhuma imagem encontrada em {class_dir}")
        selected.extend((label, path) for path in images[:samples_per_class])
    return selected


def read_image(path: Path) -> Image:
    image = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError(f"Não foi possível decodificar a imagem: {path}")
    return image


def largest_component(mask: Mask) -> Mask:
    binary = np.where(mask > 0, 255, 0).astype(np.uint8)
    count, labels, stats, _ = cv2.connectedComponentsWithStats(binary, connectivity=8)
    if count <= 1:
        return np.zeros_like(binary)
    largest = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    return np.where(labels == largest, 255, 0).astype(np.uint8)


def hsv_mask(image: Image) -> Mask:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue, saturation, value = cv2.split(hsv)
    return (
        (hue >= 20) & (hue <= 100) & (saturation >= 35) & (value >= 25)
    ).astype(np.uint8) * 255


def morph_mask(mask: Mask) -> Mask:
    open_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    close_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, open_kernel)
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, close_kernel)
    return largest_component(cleaned)


def proxy_reference_from_corners(image: Image, threshold: float = 18.0) -> Mask:
    """Estimate foreground from corner background colors; this is not a manual mask."""
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB).astype(np.float32)
    height, width = lab.shape[:2]
    patch_height = max(4, height // 16)
    patch_width = max(4, width // 16)
    patches = (
        lab[:patch_height, :patch_width],
        lab[:patch_height, -patch_width:],
        lab[-patch_height:, :patch_width],
        lab[-patch_height:, -patch_width:],
    )
    background_colors = np.stack(
        [np.median(patch.reshape(-1, 3), axis=0) for patch in patches]
    )
    distances = np.stack(
        [np.linalg.norm(lab - color, axis=2) for color in background_colors]
    )
    foreground = (np.min(distances, axis=0) > threshold).astype(np.uint8) * 255
    return morph_mask(foreground)


def segment(image: Image) -> Segmentation:
    raw = largest_component(hsv_mask(image))
    return Segmentation(
        raw=raw,
        opened_closed=morph_mask(hsv_mask(image)),
        proxy_reference=proxy_reference_from_corners(image),
    )


def overlap_scores(predicted: Mask, reference: Mask) -> tuple[float, float]:
    predicted_binary = predicted > 0
    reference_binary = reference > 0
    intersection = int(np.count_nonzero(predicted_binary & reference_binary))
    predicted_area = int(np.count_nonzero(predicted_binary))
    reference_area = int(np.count_nonzero(reference_binary))
    if predicted_area + reference_area == 0:
        return 1.0, 1.0
    dice = 2.0 * intersection / (predicted_area + reference_area)
    union = int(np.count_nonzero(predicted_binary | reference_binary))
    iou = intersection / union if union else 1.0
    return dice, iou


def extract_features(image: Image, mask: Mask) -> dict[str, float]:
    binary = mask > 0
    area = int(np.count_nonzero(binary))
    if area == 0:
        raise ValueError("Não é possível extrair características de uma máscara vazia.")

    contours, _ = cv2.findContours(
        np.where(binary, 255, 0).astype(np.uint8),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE,
    )
    perimeter = float(sum(cv2.arcLength(contour, True) for contour in contours))
    image_area = float(binary.size)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    selected_hsv = hsv[binary].astype(np.float64)
    selected_lab = lab[binary].astype(np.float64)
    texture = _masked_glcm_features(gray, binary)

    return {
        "area_px": float(area),
        "area_percent": 100.0 * area / image_area,
        "perimeter_px": perimeter,
        "circularity": 4.0 * np.pi * area / perimeter**2 if perimeter else 0.0,
        "mean_hue_opencv_0_179": float(np.mean(selected_hsv[:, 0])),
        "mean_saturation_opencv_0_255": float(np.mean(selected_hsv[:, 1])),
        "mean_value_opencv_0_255": float(np.mean(selected_hsv[:, 2])),
        "mean_lab_l_0_255": float(np.mean(selected_lab[:, 0])),
        "mean_lab_a_0_255": float(np.mean(selected_lab[:, 1])),
        "mean_lab_b_0_255": float(np.mean(selected_lab[:, 2])),
        **texture,
    }


def _masked_glcm_features(gray: Image, mask: NDArray[np.bool_]) -> dict[str, float]:
    levels = 16
    quantized = np.minimum(gray.astype(np.int32) * levels // 256, levels - 1)
    matrix = np.zeros((levels, levels), dtype=np.float64)
    for row_offset, column_offset in ((0, 1), (1, 0), (1, 1)):
        height, width = gray.shape
        first = quantized[: height - row_offset or height, : width - column_offset or width]
        second = quantized[row_offset:, column_offset:]
        first_mask = mask[: height - row_offset or height, : width - column_offset or width]
        second_mask = mask[row_offset:, column_offset:]
        valid = first_mask & second_mask
        if not np.any(valid):
            continue
        first_values = first[valid]
        second_values = second[valid]
        matrix += np.bincount(
            first_values * levels + second_values,
            minlength=levels * levels,
        ).reshape(levels, levels)
    matrix += matrix.T
    total = float(matrix.sum())
    if total == 0:
        return {
            "glcm_contrast": 0.0,
            "glcm_homogeneity": 0.0,
            "glcm_energy": 0.0,
        }
    probabilities = matrix / total
    indices = np.arange(levels, dtype=np.float64)
    differences = indices[:, None] - indices[None, :]
    return {
        "glcm_contrast": float(np.sum(probabilities * differences**2)),
        "glcm_homogeneity": float(np.sum(probabilities / (1.0 + differences**2))),
        "glcm_energy": float(np.sum(probabilities**2)),
    }
