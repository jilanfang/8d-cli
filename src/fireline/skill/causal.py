"""Causal analysis helpers: 5-Why and Escape Point.

Supports both 8d-guru field naming (layer, question) and legacy field naming
(level, why) for backward compatibility.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class ValidationResult:
    valid: bool
    reasons: list[str]


def _get_why_question(step: dict[str, Any]) -> str | None:
    """8d-guru uses ``question``, legacy uses ``why``."""
    return step.get("question") or step.get("why")


def _get_why_layer(step: dict[str, Any]) -> int | None:
    """8d-guru uses ``layer``, legacy uses ``level``."""
    return step.get("layer") or step.get("level")


def validate_why_chain(why_chain: list[dict[str, Any]]) -> ValidationResult:
    """Check that a 5-Why chain does not stop at symptom or responsibility."""
    reasons: list[str] = []
    if not why_chain:
        reasons.append("5-Why 链为空")
        return ValidationResult(valid=False, reasons=reasons)

    if len(why_chain) < 2:
        reasons.append("追问次数不足（至少需 2 层），可能停在表面现象")

    last_answer = why_chain[-1].get("answer", "").lower()
    responsibility_words = [
        "失误", "错误", "疏忽", "没注意", "责任心", "供应商", "操作员",
        "培训不足", "培训不到位", "加强管理",
    ]
    if any(word in last_answer for word in responsibility_words):
        reasons.append(f"最后一层 '{last_answer}' 看起来停在责任归属，而非控制点")

    # Check each step has required fields (support both naming conventions)
    for i, step in enumerate(why_chain):
        question = _get_why_question(step)
        answer = step.get("answer")
        if not question or not answer:
            reasons.append(f"第 {i + 1} 层缺少 why/question 或 answer")

    return ValidationResult(valid=len(reasons) == 0, reasons=reasons)


def validate_escape_chain(escape_chain: list[dict[str, Any]]) -> ValidationResult:
    """Check that escape chain traces to earliest detection point.

    Supports both 8d-guru (detection_point) and legacy (location) field names.
    """
    reasons: list[str] = []
    if not escape_chain:
        reasons.append("流出链为空")
        return ValidationResult(valid=False, reasons=reasons)

    for i, step in enumerate(escape_chain):
        location = step.get("detection_point") or step.get("location")
        why_escaped = step.get("why_escaped")
        if not location or not why_escaped:
            reasons.append(
                f"流出链第 {i + 1} 层缺少 detection_point/location 或 why_escaped"
            )

    return ValidationResult(valid=len(reasons) == 0, reasons=reasons)


def chain_confidence(
    why_chain: list[dict[str, Any]], escape_chain: list[dict[str, Any]] | None
) -> float:
    """Heuristic confidence based on chain depth and completeness."""
    score = 0.5
    if why_chain:
        score += min(0.3, (len(why_chain) - 1) * 0.1)
    if escape_chain:
        score += 0.2
    return min(1.0, score)
