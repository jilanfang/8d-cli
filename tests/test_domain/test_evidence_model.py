"""Tests for Evidence model."""

from fireline.domain.models.evidence import EvidenceBundle, EvidenceItem


def test_create_item():
    item = EvidenceItem(type="doc", ref="ref1", content="hello")
    assert item.type == "doc"
    assert item.content == "hello"


def test_bundle_summary():
    bundle = EvidenceBundle(items=[EvidenceItem(type="t", ref="r", content="c")])
    assert bundle.summary() != ""


def test_empty_bundle():
    bundle = EvidenceBundle(items=[])
    assert bundle.summary() == "（暂无证据）"
