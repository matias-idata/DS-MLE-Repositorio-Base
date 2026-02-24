from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import yaml


def load_yaml(path: str | Path) -> Dict[str, Any]:
    """Carga YAML a dict.

    Args:
        path: Ruta a archivo YAML.

    Returns:
        Diccionario con configuración.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Config no encontrada: {path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)
