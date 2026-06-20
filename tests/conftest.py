"""Shared test fixtures for 8D-CLI tests."""

import pytest

from fireline.adapters.storage.json_store import JsonStore
from fireline.config.schema import FirelineConfig
from fireline.domain.models.evidence import EvidenceBundle, EvidenceItem
from fireline.domain.models.factory import FactoryExperience


@pytest.fixture
def tmp_data_dir(tmp_path):
    """Temporary data directory for isolated test storage."""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    return data_dir


@pytest.fixture
def config(tmp_data_dir):
    """FirelineConfig with isolated data directory."""
    return FirelineConfig(data_dir=tmp_data_dir, default_factory="test_factory")


@pytest.fixture
def store(config):
    """JsonStore seeded with a factory directory."""
    s = JsonStore("test_factory", base_dir=config.data_dir)
    s.ensure_factory_dir()
    return s


@pytest.fixture
def mock_llm_client():
    """Mock LLM client that returns fixed responses."""
    from fireline.adapters.llm.client import MockLLMClient

    return MockLLMClient()


@pytest.fixture
def case_service(store):
    """CaseService backed by test store."""
    from fireline.domain.services.case_service import CaseService

    return CaseService(store)


@pytest.fixture
def base_case(store):
    """A minimal pre-created case."""
    from fireline.domain.services.case_service import CaseService

    svc = CaseService(store)
    return svc.create_case("USB 上电无输出", "test_factory")


@pytest.fixture
def evidence_bundle():
    """A simple evidence bundle with one item."""
    return EvidenceBundle(
        items=[
            EvidenceItem(
                type="cli_input",
                ref="test",
                content="USB 接口上电无输出",
                summary="USB no output",
            )
        ]
    )


@pytest.fixture
def factory_experience():
    """A minimal FactoryExperience for testing."""
    return FactoryExperience(factory_id="test_factory")


@pytest.fixture
def case_with_answers(store, base_case):
    """A case with D1 basic answers filled in."""
    from fireline.domain.services.case_service import CaseService

    svc = CaseService(store)
    svc.update_answer(base_case.case_id, "d1-q1", {"name": "张三", "role": "质量工程师"})
    svc.update_answer(base_case.case_id, "d1-q2", {"name": "李四", "role": "客户对接"})
    svc.update_answer(base_case.case_id, "d1-q3", {"name": "王五", "role": "技术负责人"})
    return svc.get_case(base_case.case_id)
