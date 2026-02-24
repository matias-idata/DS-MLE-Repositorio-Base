.PHONY: help setup install lint format test smoke demo clean

help:
	@echo "Targets:"
	@echo "  setup       - Instala deps usando requirements-dev.txt"
	@echo "  install     - Instala el proyecto en modo editable (incluye dev deps)"
	@echo "  lint        - Ruff"
	@echo "  format      - Black + Ruff (fix)"
	@echo "  test        - Unit tests"
	@echo "  smoke       - Smoke test (pipeline demo)"
	@echo "  demo        - Genera data demo, entrena, evalúa y reporta"
	@echo "  clean       - Limpia artefactos"

setup:
	pip install -U pip
	pip install -r requirements-dev.txt

install:
	pip install -U pip
	pip install -e ".[dev]"

lint:
	ruff check .

format:
	black .
	ruff check . --fix

test:
	pytest -q

smoke:
	pytest -q tests/smoke -k smoke

demo:
	python scripts/make_demo_data.py --out data/raw/demo.csv
	python scripts/train_demo.py --config configs/demo/train.yaml
	python scripts/evaluate_demo.py --config configs/demo/eval.yaml

clean:
	rm -rf .pytest_cache .ruff_cache dist build outputs
