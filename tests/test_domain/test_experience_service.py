"""Tests for ExperienceService."""


from fireline.domain.models.factory import FactoryExperience, Pattern
from fireline.domain.services.experience_service import ExperienceService


def test_get_context_for_case_empty(store, base_case):
    """When no experience is saved, returns None."""
    svc = ExperienceService(store)
    ctx = svc.get_context_for_case(base_case)
    assert ctx is None


def test_get_context_with_experience(store, base_case, factory_experience):
    store.save_experience(factory_experience)
    svc = ExperienceService(store)
    ctx = svc.get_context_for_case(base_case)
    assert ctx is not None
    assert ctx.factory_id == store.factory_id


def test_save_and_load_experience(store):
    exp = FactoryExperience(factory_id="test_factory")
    store.save_experience(exp)
    loaded = store.load_experience()
    assert loaded is not None
    assert loaded.factory_id == "test_factory"


def test_experience_with_patterns(store):
    exp = FactoryExperience(
        factory_id="test_factory",
        patterns=[
            Pattern(
                phenomenon_type="solder_crack",
                frequency="high",
                hit_count=5,
                typical_causes=[{"cause": "温度过高"}],
            )
        ],
    )
    store.save_experience(exp)
    loaded = store.load_experience()
    assert len(loaded.patterns) == 1
    assert loaded.patterns[0].phenomenon_type == "solder_crack"


def test_ensure_default_experience_creates(store):
    """ensure_default_experience creates one when none exists."""
    svc = ExperienceService(store)
    # No experience saved yet
    assert store.load_experience() is None
    exp = svc.ensure_default_experience()
    assert exp is not None
    assert exp.factory_id == store.factory_id


def test_ensure_default_experience_idempotent(store, factory_experience):
    """ensure_default_experience returns existing when already saved."""
    store.save_experience(factory_experience)
    svc = ExperienceService(store)
    exp = svc.ensure_default_experience()
    assert exp.factory_id == factory_experience.factory_id


def test_get_context_matches_phenomenon(store, base_case):
    """When a case answer matches a pattern phenomenon, the pattern is returned."""
    from fireline.domain.services.case_service import CaseService

    svc_case = CaseService(store)
    svc_case.update_answer(base_case.case_id, "d0-q1", {"phenomenon": "solder_crack"})
    case = svc_case.get_case(base_case.case_id)

    exp = FactoryExperience(
        factory_id="test_factory",
        patterns=[
            Pattern(
                phenomenon_type="solder_crack",
                frequency="high",
                hit_count=5,
                typical_causes=[{"cause": "温度过高"}],
            )
        ],
    )
    store.save_experience(exp)

    svc = ExperienceService(store)
    ctx = svc.get_context_for_case(case)
    assert ctx is not None
    assert len(ctx.patterns) == 1
    assert ctx.patterns[0].phenomenon_type == "solder_crack"
