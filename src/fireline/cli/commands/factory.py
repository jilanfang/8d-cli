"""Factory experience management commands."""

import shutil
from datetime import datetime, timezone
from pathlib import Path

import typer
import yaml
from rich.console import Console

from fireline.adapters.storage.json_store import JsonStore
from fireline.cli.context import get_preset_data_dir, get_store
from fireline.config.schema import FirelineConfig
from fireline.domain.models.factory import FactoryExperience

app = typer.Typer(name="factory", help="工厂经验层管理")
console = Console()


def _store(factory_id: str) -> JsonStore:
    return JsonStore(factory_id, base_dir=FirelineConfig().data_dir)


@app.command("init")
def init_factory(
    factory_id: str = typer.Argument(..., help="工厂 ID"),
    name: str | None = typer.Option(None, "--name", help="工厂名称"),
) -> None:
    """初始化工厂经验层。"""
    store = _store(factory_id)
    store.ensure_factory_dir()

    preset = get_preset_data_dir(factory_id)
    if preset:
        # Seed runtime data from repo preset
        target = store.factory_dir
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(preset, target)
        console.print(f"已从预设模型初始化: {factory_id}")
    elif store.load_experience() is None:
        experience = FactoryExperience(factory_id=factory_id)
        store.save_experience(experience)
        console.print(f"工厂已初始化: {factory_id}")
    else:
        console.print(f"工厂已存在: {factory_id}")

    if name:
        console.print(f"名称: {name}")


@app.command("status")
def factory_status(
    factory_id: str | None = typer.Argument(None, help="工厂 ID，默认使用配置"),
) -> None:
    """查看工厂经验成熟度。"""
    store = get_store(factory_id)
    factory_id = store.factory_id
    experience = store.load_experience()
    cases = store.list_cases()
    console.print(f"工厂: {factory_id}")
    console.print(f"  案件样本: {len(cases)}")
    if experience:
        console.print(f"  模式数: {len(experience.patterns)}")
        console.print(f"  词表数: {len(experience.vocabulary)}")
        console.print(f"  控制点画像: {len(experience.control_point_map)}")
        console.print(f"  当前模式: {experience.mode.value}")
    else:
        console.print("  经验层为空，请先运行 factory init")


LAYER_DEFINITIONS = {
    "Layer 1": {
        "label": "历史 8D / RCA / CAPA 报告",
        "dirs": {"8d_reports", "8d", "rca", "capa", "historical_8d"},
    },
    "Layer 2": {
        "label": "测试记录 / 邮件 / 图纸",
        "dirs": {"test_records", "emails", "drawings", "test_logs", "email_threads"},
    },
    "Layer 3": {
        "label": "Control Plan / PFMEA / SOP",
        "dirs": {"control_plans", "pfmea", "sop", "control_plan"},
    },
    "Layer 4": {
        "label": "BOM / 版本 / 变更记录",
        "dirs": {"bom", "versions", "change_records", "version_records"},
    },
}


@app.command("load")
def load_factory(
    factory_id: str = typer.Argument(..., help="工厂 ID"),
    path: Path = typer.Argument(..., help="四层输入协议数据目录"),
) -> None:
    """按四层输入协议扫描历史数据目录，生成分层清单。"""
    store = get_store(factory_id)
    factory_id = store.factory_id

    console.print(f"扫描输入目录: {path}")
    if not path.exists():
        console.print("[yellow]输入目录不存在[/yellow]")

    layers: dict[str, dict] = {}
    total_files = 0
    for layer_name, layer_def in LAYER_DEFINITIONS.items():
        found_dirs: list[str] = []
        files: list[str] = []
        if path.exists():
            for candidate in path.iterdir():
                if candidate.is_dir() and candidate.name in layer_def["dirs"]:
                    found_dirs.append(candidate.name)
                    for f in candidate.rglob("*"):
                        if f.is_file():
                            files.append(str(f.relative_to(path)))
        file_count = len(files)
        total_files += file_count
        layers[layer_name] = {
            "label": layer_def["label"],
            "found_dirs": found_dirs,
            "file_count": file_count,
            "files": files,
        }
        status_text = f"{file_count}份" if file_count else "未找到"
        console.print(f"  {layer_name}: {layer_def['label']} ({status_text})")

    manifest = {
        "source_path": str(path.absolute()),
        "loaded_at": datetime.now(timezone.utc).isoformat(),
        "status": "scanned",
        "total_files": total_files,
        "layers": layers,
    }
    manifest_path = store.factory_dir / "experience" / "loaded_manifest.yaml"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(yaml.safe_dump(manifest), encoding="utf-8")

    if total_files == 0:
        console.print("\n提示: 四层输入协议用于结构化加载客户历史质量数据。")
        console.print("当前为预设模式，无需真实数据即可运行 Demo。")
        console.print("使用 `8d factory status` 查看工厂经验层状态。")
    else:
        console.print(f"\n扫描完成，清单已保存: {manifest_path}")
