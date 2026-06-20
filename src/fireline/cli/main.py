"""Fireline CLI entry point."""

import typer
from rich.console import Console

from fireline.cli.commands import (
    advance,
    cases,
    close,
    config,
    factory,
    new,
    question,
    report,
    show,
)

app = typer.Typer(
    name="8d",
    help="Fireline 8D Quality Agent CLI",
    no_args_is_help=True,
)
console = Console()

app.add_typer(factory.app, name="factory", help="工厂经验层管理")
app.add_typer(config.app, name="config", help="配置管理")


@app.callback()
def main_callback(
    ctx: typer.Context,
    factory_id: str | None = typer.Option(None, "--factory", "-f", help="默认工厂 ID"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="详细输出"),
) -> None:
    """Fireline 8D Agent CLI."""
    ctx.ensure_object(dict)
    ctx.obj["factory_id"] = factory_id
    ctx.obj["verbose"] = verbose


app.command("new")(new.new)
app.command("show")(show.show)
app.command("question")(question.question)
app.command("advance")(advance.advance)
app.command("report")(report.report)
app.command("cases")(cases.cases)
app.command("close")(close.close)
