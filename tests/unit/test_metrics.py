from __future__ import annotations

import numpy as np

from project_name.evaluation.metrics import classification_metrics


def test_classification_metrics_basic():
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 1])
    m = classification_metrics(y_true, y_pred, y_proba=np.array([0.1, 0.9, 0.4, 0.2, 0.8]))
    d = m.to_dict()
    assert 0.0 <= d["accuracy"] <= 1.0
    assert 0.0 <= d["f1"] <= 1.0
