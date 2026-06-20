"""show command."""

import typer
from rich.console import Console
from rich.table import Table
from rich.tree import Tree

from fireline.cli.context import get_default_factory, get_store
from fireline.skill.question_catalog import QuestionCatalog

console = Console()


def show(
    case_id: str = typer.Argument(..., help="案件 ID"),
    factory_id: str | None = typer.Option(None, "--factory", "-f", help="工厂 ID"),
) -> None:
    """查看案件详情。"""
    factory_id = get_default_factory(factory_id)
    store = get_store(factory_id)
    case = store.load_case(case_id)
    if case is None:
        console.print(f"[red]案件不存在: {case_id}[/red]")
        raise typer.Exit(1)

    tree = Tree(f"[bold]{case.case_id}[/bold]  [{case.status.value}]")
    tree.add(f"工厂: {case.factory_id}")
    tree.add(f"创建: {case.created_at}")
    tree.add(f"更新: {case.updated_at}")

    stages = ["d0", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8"]
    for stage in stages:
        stage_node = tree.add(f"[bold]{stage.upper()}[/bold]")
        questions = QuestionCatalog.list_by_stage(stage)
        for q in questions:
            ans = case.answers.get(q.id)
            if ans is None or ans.status == "pending":
                status = "[dim]待完成[/dim]"
            elif ans.status == "in_progress":
                status = "[yellow]进行中[/yellow]"
            else:
                status = "[green]已完成[/green]"
            stage_node.add(f"{q.id} {q.name}: {status}")

    console.print(tree)

    if case.data_sources:
        table = Table(title="数据来源")
        table.add_column("类型")
        table.add_column("引用")
        table.add_column("摘要")
        for ds in case.data_sources:
            table.add_row(ds.type, ds.ref, ds.summary or "")
        console.print(table)
