"""cases command."""

import typer
from rich.console import Console
from rich.table import Table

from fireline.cli.context import get_default_factory, get_store

console = Console()


def cases(
    factory_id: str | None = typer.Option(None, "--factory", "-f", help="工厂 ID"),
) -> None:
    """列出当前工厂的所有案件。"""
    factory_id = get_default_factory(factory_id)
    store = get_store(factory_id)
    case_list = store.load_all_cases()

    if not case_list:
        console.print(f"工厂 {factory_id} 暂无案件")
        return

    table = Table(title=f"案件列表 - {factory_id}")
    table.add_column("案件 ID")
    table.add_column("状态")
    table.add_column("创建时间")
    table.add_column("现象摘要")

    for case in sorted(case_list, key=lambda c: c.created_at, reverse=True):
        phenomenon = ""
        if "d0-q1" in case.answers and case.answers["d0-q1"].value:
            phenomenon = str(case.answers["d0-q1"].value)[:40]
        table.add_row(
            case.case_id,
            case.status.value,
            case.created_at.strftime("%Y-%m-%d %H:%M"),
            phenomenon,
        )

    console.print(table)
