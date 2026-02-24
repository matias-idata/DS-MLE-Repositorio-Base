# Data

Este repositorio usa el patrón de capas:

- `data/raw/`      : datos crudos (inmutables, solo append si aplica)
- `data/interim/`  : transformaciones intermedias (limpieza, joins)
- `data/processed/`: dataset listo para modelar (features finales)

**Reglas**
- No commitear datos productivos en git.
- Para versionado de datasets grandes:
  - Opción 1: DVC (recomendado para archivos)
  - Opción 2: Delta Lake (si el stack lo soporta)

Si necesitas versionado de datos grandes, considera DVC o Delta Lake.
