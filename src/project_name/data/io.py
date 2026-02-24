from __future__ import annotations

from pathlib import Path

import pandas as pd


def read_csv(path: str | Path) -> pd.DataFrame:
    """Lee un CSV con encoding UTF-8 y retorna DataFrame."""
    return pd.read_csv(path)


def write_csv(df: pd.DataFrame, path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False)
