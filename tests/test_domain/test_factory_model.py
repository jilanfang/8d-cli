"""Tests for Factory model."""

from fireline.domain.models.factory import FactoryExperience, FactoryMode, Pattern


def test_create_experience():
    exp = FactoryExperience(factory_id="f1")
    assert exp.factory_id == "f1"
    assert exp.patterns == []


def test_create_pattern():
    p = Pattern(phenomenon_type="solder_crack", frequency="high")
    assert p.phenomenon_type == "solder_crack"


def test_mode_enum():
    assert FactoryMode.GENERAL.value == "general"
    assert FactoryMode.SPECIALIZED.value == "specialized"
