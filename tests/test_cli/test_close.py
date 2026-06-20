"""Smoke tests for close command."""

from typer.testing import CliRunner

from fireline.cli.main import app

runner = CliRunner()


def test_close_help():
    result = runner.invoke(app, ["close", "--help"])
    assert result.exit_code == 0
    assert "关闭原因" in result.output


def test_close_early_succeeds(tmp_path):
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_close_test"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    result = runner.invoke(
        app,
        ["close", case_id, "--reason", "early", "--factory", "factory_close_test"],
        env=env,
    )
    assert result.exit_code == 0
    assert "案件已关闭" in result.output
    assert "early" in result.output


def test_close_normal_blocked_without_d6(tmp_path):
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_close_normal_test"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    result = runner.invoke(
        app,
        [
            "close",
            case_id,
            "--reason",
            "normal",
            "--factory",
            "factory_close_normal_test",
        ],
        env=env,
    )
    assert result.exit_code == 0
    assert "正常关闭被阻断" in result.output
    assert "D6" in result.output
