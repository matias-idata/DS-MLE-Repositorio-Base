# DS/MLE Repositorio Base

Este repositorio es una **plantilla minimalista para clonar** y ejecutar proyectos de Data Science / Machine Learning, contiene todas las herramientas para trabajar en un estandar gobernado.

- Estructura estándar y simple (`/data`, `/notebooks`, `/src`, `/tests`, `/scripts`, `/outputs`)
- Gestión de datos por capas (`raw/processed`)
- Evaluación y métricas (scoring + reporte Markdown)
- Pruebas básicas (unitarias + smoke) y lint/format
- Makefile/CLI y ambientes reproducibles

> Nota: La plantilla incluye un **pipeline de ejemplo** (tabular + scikit-learn) para validar el flujo end-to-end.

## Quickstart (local)

### Instalación rápida
Si no quieres lidiar con `pyproject.toml`, usa `requirements.txt`:
```bash
python -m venv .venv
source .venv/bin/activate
make setup
```

### 1) Crear ambiente
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e ".[dev]"
```

### 2) Ejecutar pipeline demo (genera data, entrena, evalúa y genera reporte)
```bash
make demo
```

Salidas:
- `data/raw/demo.csv` (dataset demo)
- `outputs/demo/model.joblib` (modelo entrenado)
- `outputs/demo/metrics.json` y `outputs/demo/report.md` (métricas + reporte)

## Comandos principales
```bash
make help
make lint
make format
make test
make smoke
```

## Estructura
```
data/          # datasets (raw/interim/processed)
notebooks/     # exploración y prototipos
src/           # código reutilizable
tests/         # unit + smoke tests
scripts/       # pipeline demo
outputs/       # artefactos de salida (modelos, métricas, reportes)
```
