from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from project_name.config import load_yaml
from project_name.data.io import read_csv
from project_name.models.train import save_model, train_logistic_regression
from project_name.utils.logging import get_logger
from project_name.utils.paths import ensure_dir

logger = get_logger("train_demo")


def main(config_path: str) -> None:
    cfg = load_yaml(config_path)
    df: pd.DataFrame = read_csv(cfg["data"]["raw_path"])

    result = train_logistic_regression(
        df=df,
        params=cfg["model"]["params"],
        random_state=int(cfg.get("random_state", 42)),
    )

    model_path = cfg["output"]["model_path"]
    ensure_dir(Path(model_path).parent)
    save_model(result.model, model_path)

    logger.info("Modelo guardado en %s", model_path)
    logger.info("Features: %s", list(result.X_train.columns))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    main(args.config)
