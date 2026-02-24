from __future__ import annotations

import typer

from project_name.config import load_yaml

app = typer.Typer(help="CLI DS/MLE PoC Template")


@app.command()
def show_config(path: str):
    """Imprime un YAML de configuración."""
    cfg = load_yaml(path)
    typer.echo(cfg)


if __name__ == "__main__":
    app()
