import numpy as np
import pytest

from tomato_pdi.pipeline import extract_features, overlap_scores


def test_overlap_scores_for_identical_masks() -> None:
    mask = np.zeros((12, 12), dtype=np.uint8)
    mask[2:9, 3:10] = 255

    assert overlap_scores(mask, mask) == (1.0, 1.0)


def test_overlap_scores_for_disjoint_masks() -> None:
    first = np.zeros((12, 12), dtype=np.uint8)
    second = np.zeros((12, 12), dtype=np.uint8)
    first[1:4, 1:4] = 255
    second[8:11, 8:11] = 255

    assert overlap_scores(first, second) == (0.0, 0.0)


def test_extract_features_reports_area_and_texture() -> None:
    image = np.full((32, 32, 3), 120, dtype=np.uint8)
    mask = np.zeros((32, 32), dtype=np.uint8)
    mask[8:24, 8:24] = 255

    features = extract_features(image, mask)

    assert features["area_px"] == 256
    assert features["area_percent"] == pytest.approx(25.0)
    assert features["perimeter_px"] > 0
    assert features["glcm_homogeneity"] == pytest.approx(1.0)
    assert features["glcm_contrast"] == pytest.approx(0.0)


def test_extract_features_rejects_empty_mask() -> None:
    image = np.zeros((8, 8, 3), dtype=np.uint8)
    mask = np.zeros((8, 8), dtype=np.uint8)

    with pytest.raises(ValueError, match="máscara vazia"):
        extract_features(image, mask)
