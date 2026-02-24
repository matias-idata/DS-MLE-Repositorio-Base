from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from project_name.features.build_features import build_features


@dataclass
class TrainResult:
    model: Any
    X_train: pd.DataFrame
    X_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series


def train_logistic_regression(
    df: pd.DataFrame,
    params: Dict[str, Any],
    random_state: int = 42,
    test_size: float = 0.2,
) -> TrainResult:
    X, y = build_features(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    model = LogisticRegression(**params)
    model.fit(X_train, y_train)
    return TrainResult(model=model, X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)


def save_model(model: Any, path: str) -> None:
    joblib.dump(model, path)


def load_model(path: str) -> Any:
    return joblib.load(path)
