"""close command."""

import typer
from rich.console import Console

from fireline.cli.context import get_default_factory, get_store
from fireline.domain.models.case import CaseStatus, CloseReason
from fireline.domain.services.case_service import CaseService
from fireline.domain.services.gate_service import GateService

console = Console()


def close(
    case_id: str = typer.Argument(..., help="案件 ID"),
    reason: str = typer.Option(
        "normal",
        "--reason",
        help="关闭原因: normal|early|cancelled",
    ),
    factory_id: str | None = typer.Option(None, "--factory", "-f", help="工厂 ID"),
) -> None:
    """关闭案件。normal 关闭需 D6 验证通过；early/cancelled 可跳过。"""
    factory_id = get_default_factory(factory_id)
    store = get_store(factory_id)
    case_service = CaseService(store)
    case = case_service.get_case(case_id)
    if case is None:
        console.print(f"[red]案件不存在: {case_id}[/red]")
        raise typer.Exit(1)

    close_reason = CloseReason(reason)

    if close_reason == CloseReason.NORMAL:
        gate_service = GateService()
        can_close, blockers = gate_service.can_advance(case, CaseStatus.CLOSED)
        if not can_close:
            console.print("[yellow]正常关闭被阻断[/yellow]")
            for b in blockers:
                console.print(f"  - {b}")
            return

    case.status = CaseStatus.CLOSED
    case.close_reason = close_reason
    case_service.update_answer(case_id, "status", case.status.value)
    console.print(f"[green]案件已关闭: {case_id}[/green]")
    console.print(f"关闭原因: {close_reason.value}")
