"""advance command."""

import typer
from rich.console import Console

from fireline.adapters.llm.client import make_llm_client
from fireline.cli.context import get_default_factory, get_store
from fireline.config.schema import FirelineConfig
from fireline.domain.models.case import CaseStatus
from fireline.domain.services.case_service import CaseService
from fireline.domain.services.gate_service import GateService

console = Console()


def advance(
    case_id: str = typer.Argument(..., help="案件 ID"),
    target: str = typer.Option("d5_d8", "--target", help="目标状态: d5_d8 | closed"),
    factory_id: str | None = typer.Option(None, "--factory", "-f", help="工厂 ID"),
    mock: bool = typer.Option(False, "--mock", help="使用 Mock LLM，不调用真实 API"),
) -> None:
    """尝试推进案件阶段。"""
    factory_id = get_default_factory(factory_id)
    store = get_store(factory_id)
    case_service = CaseService(store)
    case = case_service.get_case(case_id)
    if case is None:
        console.print(f"[red]案件不存在: {case_id}[/red]")
        raise typer.Exit(1)

    # Ensure llm client is created (not strictly needed for gate service, but keeps signature)
    _ = make_llm_client(FirelineConfig().llm, mock=mock)

    gate_service = GateService()
    target_status = CaseStatus(target)
    can_advance, blockers = gate_service.can_advance(case, target_status)

    if not can_advance:
        console.print("[yellow]推进被阻断[/yellow]")
        for b in blockers:
            console.print(f"  - {b}")
        return

    case.status = target_status
    case_service.update_answer(case_id, "status", target_status.value)
    console.print(f"[green]案件已推进到: {target_status.value}[/green]")
