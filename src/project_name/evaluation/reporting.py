from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from project_name.utils.paths import ensure_dir


def write_metrics(metrics: Dict[str, Any], path: str | Path) -> None:
    p = Path(path)
    ensure_dir(p.parent)
    p.write_text(json.dumps(metrics, indent=2, ensure_ascii=False), encoding="utf-8")


def write_markdown_report(summary: Dict[str, Any], path: str | Path) -> None:
    p = Path(path)
    ensure_dir(p.parent)
    lines = [
        f"# Reporte de Evaluación — {summary.get('project','(sin nombre)')}\n",
        "## Resumen\n",
    ]
    for k, v in summary.get("metrics", {}).items():
        lines.append(f"- **{k}**: {v}\n")
    lines.append("\n## Trazabilidad\n")
    for k, v in summary.get("trace", {}).items():
        lines.append(f"- {k}: {v}\n")
    p.write_text("".join(lines), encoding="utf-8")
