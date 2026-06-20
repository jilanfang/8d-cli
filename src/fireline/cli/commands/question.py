"""question command."""

import asyncio

import typer
from rich.console import Console

from fireline.adapters.llm.client import make_llm_client
from fireline.cli.context import get_default_factory, get_store
from fireline.config.schema import FirelineConfig
from fireline.domain.services.case_service import CaseService
from fireline.domain.services.experience_service import ExperienceService
from fireline.domain.services.question_service import QuestionService

console = Console()


def question(
    case_id: str = typer.Argument(..., help="案件 ID"),
    question_id: str = typer.Argument(..., help="问题点 ID，例如 d0-q3"),
    factory_id: str | None = typer.Option(None, "--factory", "-f", help="工厂 ID"),
    mock: bool = typer.Option(False, "--mock", help="使用 Mock LLM，不调用真实 API"),
    answer: str | None = typer.Option(
        None, "--answer", "-a", help="直接提供回答内容（JSON 字符串）"
    ),
) -> None:
    """触发问题点引导；如提供 --answer 则保存回答。"""
    factory_id = get_default_factory(factory_id)
    store = get_store(factory_id)
    case_service = CaseService(store)
    case = case_service.get_case(case_id)
    if case is None:
        console.print(f"[red]案件不存在: {case_id}[/red]")
        raise typer.Exit(1)

    if answer:
        import json

        try:
            value = json.loads(answer)
        except json.JSONDecodeError:
            value = answer
        updated = case_service.update_answer(case_id, question_id, value)
        console.print(f"已保存 {question_id}")
        console.print(f"当前状态: {updated.status.value}")
        return

    cfg = FirelineConfig()
    client = make_llm_client(cfg.llm, mock=mock)
    exp_service = ExperienceService(store)
    experience = exp_service.get_context_for_case(case)
    q_service = QuestionService(
        client, skill_path=cfg.skill.skill_path, skill_profiles=cfg.skill.profiles
    )
    result = asyncio.run(q_service.guide(case, question_id, experience))

    console.print(f"## [{question_id}] 引导")
    console.print(result["prompt_text"])
    console.print(
        f"\n[dim]gate_status: {result['gate_status']}, confidence: {result['confidence']}[/dim]"
    )
    if result["next_actions"]:
        console.print("\n建议下一步:")
        for action in result["next_actions"]:
            console.print(f"  - {action}")
    console.print("\n保存回答示例：")
    console.print(f'  8d question {case_id} {question_id} --answer \'{{"answer":"..."}}\'')
