"""Evidence bundle model passed between CLI and Skill."""

from typing import Any

from pydantic import BaseModel, Field


class EvidenceItem(BaseModel):
    type: str
    ref: str
    summary: str | None = None
    content: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class EvidenceBundle(BaseModel):
    items: list[EvidenceItem] = Field(default_factory=list)

    def summary(self) -> str:
        lines = []
        for item in self.items:
            line = f"- [{item.type}] {item.ref}"
            if item.summary:
                line += f": {item.summary}"
            lines.append(line)
        return "\n".join(lines) if lines else "（暂无证据）"
