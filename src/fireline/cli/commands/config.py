"""Configuration management commands."""

import typer
from rich.console import Console

from fireline.config.schema import load_user_config, save_user_config

app = typer.Typer(name="config", help="配置管理")
console = Console()


@app.command("factory")
def config_factory(
    factory_id: str = typer.Argument(..., help="默认工厂 ID"),
) -> None:
    """设置默认工厂，写入 ~/.fireline/config.json。"""
    config = load_user_config()
    config["default_factory"] = factory_id
    save_user_config(config)
    console.print(f"默认工厂已设置为: {factory_id}")
    console.print("配置文件: ~/.fireline/config.json")
