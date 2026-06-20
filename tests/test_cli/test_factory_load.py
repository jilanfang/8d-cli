"""Smoke tests for factory load command."""

from typer.testing import CliRunner

from fireline.cli.main import app

runner = CliRunner()


def test_factory_load_help():
    result = runner.invoke(app, ["factory", "load", "--help"])
    assert result.exit_code == 0
    assert "四层输入协议" in result.output


def test_factory_load_empty_directory(tmp_path):
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    empty_dir = tmp_path / "empty_data"
    empty_dir.mkdir()
    result = runner.invoke(
        app,
        ["factory", "load", "factory_load_test", str(empty_dir)],
        env=env,
    )
    assert result.exit_code == 0
    assert "Layer 1" in result.output
    assert "未找到" in result.output
    assert "预设模式" in result.output


def test_factory_load_with_layer_directories(tmp_path):
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    data_dir = tmp_path / "quality_data"
    (data_dir / "8d_reports").mkdir(parents=True)
    (data_dir / "8d_reports" / "8D-2026-001.md").write_text("# 8D")
    (data_dir / "test_records").mkdir(parents=True)
    (data_dir / "test_records" / "test.log").write_text("pass")

    result = runner.invoke(
        app,
        ["factory", "load", "factory_load_test", str(data_dir)],
        env=env,
    )
    assert result.exit_code == 0
    assert "Layer 1" in result.output
    assert "1份" in result.output or "0份" in result.output
    assert "扫描完成" in result.output
