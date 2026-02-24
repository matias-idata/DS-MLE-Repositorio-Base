from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def main(out: str) -> None:
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(42)
    n = 800
    f1 = rng.normal(0, 1, n)
    f2 = rng.normal(0, 1, n)
    f3 = rng.normal(0, 1, n)
    # etiqueta con señal
    logits = 0.8 * f1 - 0.6 * f2 + 0.3 * f3
    p = 1 / (1 + np.exp(-logits))
    y = (rng.random(n) < p).astype(int)

    df = pd.DataFrame({"f1": f1, "f2": f2, "f3": f3, "label": y})
    df.to_csv(out, index=False)
    print(f"[OK] demo data -> {out} ({df.shape[0]} filas)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    main(args.out)
