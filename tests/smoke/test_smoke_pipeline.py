from __future__ import annotations

import subprocess
from pathlib import Path


def test_smoke_demo_pipeline_runs():
    root = Path(__file__).resolve().parents[2]
    # run demo targets quickly
    r = subprocess.run(["make", "demo"], cwd=root, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr

    assert (root / "data/raw/demo.csv").exists()
    assert (root / "models/demo/model.joblib").exists()
    assert (root / "reports/demo/metrics.json").exists()
    assert (root / "reports/demo/report.md").exists()
