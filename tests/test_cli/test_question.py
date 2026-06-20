"""Smoke tests for CLI question command — guidance and answer modes."""

from typer.testing import CliRunner

from fireline.cli.main import app

runner = CliRunner()


def test_question_help():
    result = runner.invoke(app, ["question", "--help"])
    assert result.exit_code == 0
    assert "问题点 ID" in result.output


def test_question_guide_mock(tmp_path):
    """Mock mode triggers LLM-guided question output."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_question_guide"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    result = runner.invoke(
        app,
        ["question", case_id, "d0-q1", "--mock", "--factory", "factory_question_guide"],
        env=env,
    )
    assert result.exit_code == 0
    assert "引导" in result.output


def test_question_save_answer_json(tmp_path):
    """--answer with JSON string saves structured answer."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_question_json"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    result = runner.invoke(
        app,
        [
            "question",
            case_id,
            "d0-q1",
            "--answer",
            '{"phenomenon": "USB no output"}',
            "--factory",
            "factory_question_json",
        ],
        env=env,
    )
    assert result.exit_code == 0
    assert "已保存" in result.output


def test_question_save_answer_plain_text(tmp_path):
    """--answer with plain text (not JSON) still saves."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_question_plain"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    result = runner.invoke(
        app,
        [
            "question",
            case_id,
            "d0-q1",
            "--answer",
            "plain text answer",
            "--factory",
            "factory_question_plain",
        ],
        env=env,
    )
    assert result.exit_code == 0
    assert "已保存" in result.output


def test_question_invalid_qid(tmp_path):
    """Invalid question_id should error (KeyError from QuestionCatalog)."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_question_invalid"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    result = runner.invoke(
        app,
        ["question", case_id, "invalid-q99", "--mock", "--factory", "factory_question_invalid"],
        env=env,
    )
    assert result.exit_code != 0


def test_question_missing_case(tmp_path):
    """Non-existent case should show error and exit 1."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    args = [
        "question", "CASE-NONEXISTENT", "d0-q1",
        "--mock", "--factory", "factory_question_missing",
    ]
    result = runner.invoke(app, args, env=env)
    assert result.exit_code == 1
    assert "不存在" in result.output


def test_question_d4q3_mock(tmp_path):
    """D4-Q3 (5-Why root cause) guidance triggers correctly."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_question_d4q3"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    result = runner.invoke(
        app,
        ["question", case_id, "d4-q3", "--mock", "--factory", "factory_question_d4q3"],
        env=env,
    )
    assert result.exit_code == 0
    assert "引导" in result.output


def test_question_with_factory_flag(tmp_path):
    """--factory flag explicitly overrides default factory."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_question_flag"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    result = runner.invoke(
        app,
        ["question", case_id, "d0-q1", "--mock", "--factory", "factory_question_flag"],
        env=env,
    )
    assert result.exit_code == 0
    assert "引导" in result.output
