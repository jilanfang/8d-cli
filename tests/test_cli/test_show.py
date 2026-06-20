"""Smoke tests for CLI show command and new/show integration."""

from typer.testing import CliRunner

from fireline.cli.main import app

runner = CliRunner()


def test_show_help():
    result = runner.invoke(app, ["show", "--help"])
    assert result.exit_code == 0
    assert "案件 ID" in result.output


def test_new_then_show_finds_case(tmp_path):
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_show_test"],
        env=env,
    )
    assert new_result.exit_code == 0
    assert "案件已创建" in new_result.output

    # Extract case id from output line like "案件已创建: CASE-..."
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    show_result = runner.invoke(
        app, ["show", case_id, "--factory", "factory_show_test"], env=env
    )
    assert show_result.exit_code == 0
    assert case_id in show_result.output
    assert "cli_input" in show_result.output


def test_show_missing_case(tmp_path):
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    result = runner.invoke(
        app, ["show", "CASE-NOT-EXIST", "--factory", "factory_show_test"], env=env
    )
    assert result.exit_code != 0
    assert "案件不存在" in result.output
