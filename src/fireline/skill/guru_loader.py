"""Guru data loader — reads 8d-guru markdown from bundled package data.

This replaces the external-path ``MarkdownSkillLoader``. All 8d-guru
methodology files (42 prompts, constraints, gates, deliverables, patterns,
profiles) are embedded as package data at install time.
"""

from __future__ import annotations

import json
from importlib.resources import files
from typing import Any


class GuruDataLoader:
    """Read embedded 8d-guru methodology files.

    All files are bundled as package data under ``fireline.skill.guru_data``.
    No external path needed — the methodology ships with the CLI.
    """

    def __init__(self):
        self._root = files("fireline.skill") / "guru_data"

    def _read(self, *parts: str) -> str:
        p = self._root.joinpath(*parts)
        if not p.is_file():
            raise FileNotFoundError(f"Guru data file not bundled: {'/'.join(parts)}")
        return p.read_text(encoding="utf-8")

    # ── prompt loading ──────────────────────────────────────────────

    def load_question_prompt(self, question_id: str) -> str:
        """Read a question-point prompt (e.g. ``d4-q3``, ``intake``)."""
        return self._read("docs", "prompts", f"{question_id}.md")

    def load_intake_prompt(self) -> str:
        return self.load_question_prompt("intake")

    # ── methodology docs ────────────────────────────────────────────

    def load_stage_methodology(self, stage: str) -> str:
        return self._read("docs", "methodology", f"{stage}.md")

    def load_constraints(self) -> str:
        try:
            return self._read("constraints.txt")
        except FileNotFoundError:
            return ""

    # ── gates & deliverables ────────────────────────────────────────

    def load_gate_rules(self) -> str:
        return self._read("docs", "gates.md")

    def load_deliverable_templates(self) -> str:
        return self._read("docs", "deliverables.md")

    # ── enhancement tools ───────────────────────────────────────────

    def load_pattern(self, name: str) -> str:
        return self._read("docs", "patterns", f"{name}.md")

    # ── industry profiles ───────────────────────────────────────────

    def detect_profile(self, user_input: str) -> str | None:
        text = user_input.lower()
        iatf_kw = ["iatf", "16949", "ppap", "oem", "汽车", "automotive", "aiag", "vda"]
        iso_kw = ["iso 9001", "iso9001", "质量管理体系", "内审", "外审", "qms", "9001"]
        for kw in iatf_kw:
            if kw in text:
                return "iatf16949"
        for kw in iso_kw:
            if kw in text:
                return "iso9001"
        return None

    def load_profile_overlay(self, profile: str) -> str:
        return self._read("profiles", profile, "overlay.md")

    # ── prompt assembly ─────────────────────────────────────────────

    def assemble_question_prompt(
        self,
        question_id: str,
        case_state: dict[str, Any],
        evidence: list[dict[str, Any]] | None = None,
        experience_text: str = "",
        profile: str | None = None,
    ) -> str:
        """Assemble a complete prompt for a question point."""
        parts: list[str] = []

        constraints = self.load_constraints()
        if constraints:
            parts.append(constraints)

        parts.append("## 当前案例状态\n")
        parts.append(json.dumps(case_state, ensure_ascii=False, indent=2))

        if evidence:
            parts.append("\n## 证据\n")
            parts.append(json.dumps(evidence, ensure_ascii=False, indent=2))

        if experience_text:
            parts.append("\n## 工厂经验\n")
            parts.append(experience_text)

        if profile:
            try:
                parts.append("\n## 行业规范叠加\n")
                parts.append(self.load_profile_overlay(profile))
            except FileNotFoundError:
                pass

        parts.append("\n---\n")
        parts.append(self.load_question_prompt(question_id))

        return "\n".join(parts)

    def assemble_intake_prompt(
        self,
        raw_input: str,
        case_state: dict[str, Any] | None = None,
        profile: str | None = None,
    ) -> str:
        """Assemble a complete intake / triage prompt."""
        parts: list[str] = []

        constraints = self.load_constraints()
        if constraints:
            parts.append(constraints)

        if case_state:
            parts.append("## 案例状态\n")
            parts.append(json.dumps(case_state, ensure_ascii=False, indent=2))

        parts.append(f"\n## 用户原始输入\n\n{raw_input}")

        if profile:
            try:
                parts.append("\n## 行业规范叠加\n")
                parts.append(self.load_profile_overlay(profile))
            except FileNotFoundError:
                pass

        parts.append("\n---\n")
        parts.append(self.load_intake_prompt())

        return "\n".join(parts)
