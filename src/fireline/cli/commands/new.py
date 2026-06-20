"""new command."""

import asyncio

import typer
from rich.console import Console

from fireline.adapters.llm.client import make_llm_client
from fireline.cli.context import get_default_factory, get_store
from fireline.config.schema import FirelineConfig
from fireline.domain.services.intake_service import IntakeService

console = Console()


def new(
    raw_input: str = typer.Argument(..., help="原始输入"),
    factory_id: str | None = typer.Option(None, "--factory", "-f", help="工厂 ID"),
    mock: bool = typer.Option(False, "--mock", help="使用 Mock LLM，不调用真实 API"),
) -> None:
    """从原始输入创建案件。"""
    factory_id = get_default_factory(factory_id)
    # Seed preset factory data before intake creates its own directory.
    get_store(factory_id)
    cfg = FirelineConfig()
    client = make_llm_client(cfg.llm, mock=mock)
    service = IntakeService(client, base_dir=cfg.data_dir)
    case, follow_ups = asyncio.run(service.process(raw_input, factory_id))

    console.print(f"案件已创建: {case.case_id}")
    if follow_ups:
        console.print("建议追问:")
        for qid in follow_ups:
            console.print(f"  - {qid}")
    console.print(f"使用 `8d show {case.case_id}` 查看详情")
