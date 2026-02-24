from __future__ import annotations

import pandas as pd


def build_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Ejemplo simple: separa X/y y aplica una transformación mínima.

    Espera columnas: f1, f2, f3, label
    """
    required = {"f1", "f2", "f3", "label"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {sorted(missing)}")

    X = df[["f1", "f2", "f3"]].copy()
    y = df["label"].astype(int)

    # Ejemplo: feature derivada
    X["f_sum"] = X["f1"] + X["f2"] + X["f3"]
    return X, y
