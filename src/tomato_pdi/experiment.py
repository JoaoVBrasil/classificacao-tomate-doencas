from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import cv2
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from .pipeline import (
    discover_images,
    extract_features,
    overlap_scores,
    read_image,
    segment,
)


def run_experiment(
    dataset_dir: Path,
    output_dir: Path,
    samples_per_class: int = 12,
) -> dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    selected = discover_images(dataset_dir, samples_per_class)
    metric_rows: list[dict[str, object]] = []
    feature_rows: list[dict[str, object]] = []
    examples: list[tuple[str, Path, np.ndarray, object]] = []

    for label, path in selected:
        image = read_image(path)
        results = segment(image)
        raw_dice, raw_iou = overlap_scores(results.raw, results.proxy_reference)
        morph_dice, morph_iou = overlap_scores(
            results.opened_closed,
            results.proxy_reference,
        )
        metric_rows.append(
            {
                "classe": label,
                "imagem": path.name,
                "configuracao": "HSV_abertura_3x3_fechamento_5x5",
                "dice_proxy": morph_dice,
                "iou_proxy": morph_iou,
                "dice_sem_morfologia": raw_dice,
                "iou_sem_morfologia": raw_iou,
                "area_mascara_px": int(np.count_nonzero(results.opened_closed)),
                "area_referencia_proxy_px": int(
                    np.count_nonzero(results.proxy_reference)
                ),
            }
        )
        feature_rows.append(
            {
                "classe": label,
                "imagem": path.name,
                **extract_features(image, results.opened_closed),
            }
        )
        examples.append((label, path, image, results))

    _write_csv(output_dir / "segmentacao_metricas.csv", metric_rows)
    _write_csv(output_dir / "descritores.csv", feature_rows)
    summary = _summary(metric_rows, len(selected), samples_per_class)
    (output_dir / "resumo.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    _plot_summary(output_dir / "comparacao_morfologia.png", metric_rows)
    _plot_examples(output_dir / "mascaras_exemplo.png", examples, metric_rows)
    return summary


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError("Não há resultados para gravar.")
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _summary(
    rows: list[dict[str, object]],
    image_count: int,
    samples_per_class: int,
) -> dict[str, object]:
    return {
        "imagens_avaliadas": image_count,
        "imagens_por_classe": samples_per_class,
        "referencia": "proxy automatico por cor de fundo estimada nos quatro cantos",
        "aviso": "Dice/IoU medem concordancia com o proxy, nao com anotacao manual.",
        "sem_morfologia": {
            "dice_medio": float(np.mean([row["dice_sem_morfologia"] for row in rows])),
            "iou_medio": float(np.mean([row["iou_sem_morfologia"] for row in rows])),
        },
        "abertura_fechamento": {
            "dice_medio": float(np.mean([row["dice_proxy"] for row in rows])),
            "iou_medio": float(np.mean([row["iou_proxy"] for row in rows])),
        },
    }


def _plot_summary(path: Path, rows: list[dict[str, object]]) -> None:
    configs = (
        ("Sem morfologia", "dice_sem_morfologia", "iou_sem_morfologia"),
        ("Abertura 3x3 + fechamento 5x5", "dice_proxy", "iou_proxy"),
    )
    labels = [config[0] for config in configs]
    dice = [np.mean([row[config[1]] for row in rows]) for config in configs]
    iou = [np.mean([row[config[2]] for row in rows]) for config in configs]
    positions = np.arange(len(labels))
    width = 0.36
    figure, axis = plt.subplots(figsize=(8, 4.5))
    axis.bar(positions - width / 2, dice, width, label="Dice")
    axis.bar(positions + width / 2, iou, width, label="IoU")
    axis.set_xticks(positions, labels)
    axis.set_ylim(0, 1)
    axis.set_ylabel("Média em relação ao proxy (0–1)")
    axis.set_title("Morfologia e concordância com a referência automática")
    axis.legend()
    axis.grid(axis="y", alpha=0.25)
    figure.tight_layout()
    figure.savefig(path, dpi=160)
    plt.close(figure)


def _plot_examples(
    path: Path,
    examples: list[tuple[str, Path, np.ndarray, object]],
    metric_rows: list[dict[str, object]],
) -> None:
    ordered = sorted(
        zip(examples, metric_rows),
        key=lambda item: float(item[1]["dice_proxy"]),
    )
    chosen = [ordered[0], ordered[-1]]
    figure, axes = plt.subplots(
        2,
        5,
        figsize=(14, 9),
        gridspec_kw={"width_ratios": (1.3, 1, 1, 1, 1)},
    )
    for row_index, (example, metric) in enumerate(chosen):
        label, image_path, image, result = example
        row_label = axes[row_index, 0]
        row_label.axis("off")
        row_label.text(
            0.5,
            0.5,
            (
                f"{'Menor' if row_index == 0 else 'Maior'} Dice\n"
                f"{label}\n{image_path.name}\n"
                f"{float(metric['dice_proxy']):.3f}"
            ),
            fontsize=8,
            ha="center",
            va="center",
            wrap=True,
        )
        images = (
            (cv2.cvtColor(image, cv2.COLOR_BGR2RGB), "Original"),
            (result.proxy_reference, "Proxy de referência"),
            (result.raw, "HSV sem morfologia"),
            (result.opened_closed, "HSV + abertura/fechamento"),
        )
        for axis, (content, title) in zip(axes[row_index, 1:], images):
            axis.imshow(content, cmap="gray" if content.ndim == 2 else None)
            axis.set_title(title)
            axis.axis("off")
    figure.suptitle("Casos de menor e maior concordância com o proxy")
    figure.tight_layout(rect=(0, 0, 1, 0.95), h_pad=3, w_pad=1)
    figure.savefig(path, dpi=160)
    plt.close(figure)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Executa o experimento M2 de segmentação e extração de descritores."
    )
    parser.add_argument(
        "--dataset-dir",
        type=Path,
        default=Path("images/tomato_subset"),
        help="Pasta local com as subpastas das quatro classes.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("results/m2"),
        help="Diretório em que CSVs, JSON e figuras serão gravados.",
    )
    parser.add_argument(
        "--samples-per-class",
        type=int,
        default=12,
        help="Quantidade determinística de imagens por classe (padrão: 12).",
    )
    arguments = parser.parse_args()
    summary = run_experiment(
        arguments.dataset_dir,
        arguments.output_dir,
        arguments.samples_per_class,
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
