from __future__ import annotations

import argparse
from pathlib import Path

from project_name.config import load_yaml
from project_name.data.io import read_csv
from project_name.evaluation.metrics import classification_metrics
from project_name.evaluation.reporting import write_markdown_report, write_metrics
from project_name.models.train import load_model, train_logistic_regression
from project_name.utils.logging import get_logger
from project_name.utils.paths import ensure_dir

logger = get_logger("evaluate_demo")


def main(config_path: str) -> None:
    cfg = load_yaml(config_path)

    df = read_csv(cfg["data"]["raw_path"])
    model = load_model(cfg["model"]["model_path"])

    # reproducimos split del training para demo (en prod, usar dataset/split versionado)
    split = train_logistic_regression(df=df, params={"max_iter": 1}, random_state=42)
    X_test = split.X_test
    y_test = split.y_test

    y_pred = model.predict(X_test)
    y_proba = None
    if hasattr(model, "predict_proba"):
        y_proba = model.predict_proba(X_test)[:, 1]

    m = classification_metrics(y_test, y_pred, y_proba).to_dict()

    reports_dir = Path(cfg["output"]["reports_dir"])
    ensure_dir(reports_dir)

    write_metrics({"project": cfg["project"], "metrics": m}, cfg["output"]["metrics_path"])
    write_markdown_report(
        {
            "project": cfg["project"],
            "metrics": m,
            "trace": {
                "model_path": cfg["model"]["model_path"],
                "data_path": cfg["data"]["raw_path"],
            },
        },
        cfg["output"]["report_md_path"],
    )

    logger.info("Reporte -> %s", cfg["output"]["report_md_path"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    main(args.config)
