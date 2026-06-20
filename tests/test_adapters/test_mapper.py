"""Tests for skill mapper adapter."""

from fireline.adapters.skill.mapper import (
    map_case_to_skill,
    map_evidence_to_skill,
    map_experience_to_skill,
)
from fireline.domain.models.case import Answer, Case
from fireline.domain.models.evidence import EvidenceBundle, EvidenceItem
from fireline.domain.models.factory import FactoryExperience, Pattern


def test_map_case_empty():
    case = Case(case_id="TEST-001", factory_id="f1")
    skill_case = map_case_to_skill(case)
    assert skill_case.case_id == "TEST-001"
    assert skill_case.answers == {}


def test_map_case_with_answers():
    case = Case(case_id="TEST-002", factory_id="f1")
    case.answers["d0-q1"] = Answer(value={"phenomenon": "test"}, status="complete")
    skill_case = map_case_to_skill(case)
    assert "d0-q1" in skill_case.answers
    assert skill_case.answers["d0-q1"].value == {"phenomenon": "test"}


def test_map_evidence_empty():
    bundle = EvidenceBundle(items=[])
    skill_bundle = map_evidence_to_skill(bundle)
    assert len(skill_bundle.items) == 0


def test_map_evidence_with_items():
    bundle = EvidenceBundle(
        items=[EvidenceItem(type="test", ref="r1", content="hello", summary="sum")]
    )
    skill_bundle = map_evidence_to_skill(bundle)
    assert len(skill_bundle.items) == 1
    assert skill_bundle.items[0].content == "hello"


def test_map_experience_none():
    result = map_experience_to_skill(None)
    assert result is None


def test_map_experience_full():
    exp = FactoryExperience(factory_id="f1")
    result = map_experience_to_skill(exp)
    assert result is not None
    assert result.factory_id == "f1"


def test_map_experience_with_patterns():
    exp = FactoryExperience(
        factory_id="f1",
        patterns=[
            Pattern(phenomenon_type="solder_crack", frequency="high", hit_count=3),
        ],
    )
    result = map_experience_to_skill(exp)
    assert len(result.patterns) == 1
    assert result.patterns[0].phenomenon_type == "solder_crack"
