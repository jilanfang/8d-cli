"""report command."""

import typer
from rich.console import Console

from fireline.cli.context import get_default_factory, get_store
from fireline.domain.services.case_service import CaseService
from fireline.domain.services.report_service import ReportService

console = Console()


def report(
    case_id: str = typer.Argument(..., help="案件 ID"),
    format: str = typer.Option("8d", "--format", help="报告格式: 8d|rca|capa"),
    factory_id: str | None = typer.Option(None, "--factory", "-f", help="工厂 ID"),
    mock: bool = typer.Option(False, "--mock", help="使用 Mock LLM，不调用真实 API"),
) -> None:
    """生成报告草案。"""
    factory_id = get_default_factory(factory_id)
    store = get_store(factory_id)
    case_service = CaseService(store)
    case = case_service.get_case(case_id)
    if case is None:
        console.print(f"[red]案件不存在: {case_id}[/red]")
        raise typer.Exit(1)

    service = ReportService()
    report_obj = service.generate(case, format)

    console.print(f"# {report_obj.report_id} ({report_obj.format.value.upper()})")
    for section in report_obj.sections:
        console.print(section.content)
