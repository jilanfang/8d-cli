"""Case service."""

from datetime import datetime, timezone
from typing import Any

from fireline.adapters.storage.json_store import JsonStore
from fireline.domain.models.case import Case, CaseStatus, DataSource


class CaseService:
    def __init__(self, store: JsonStore):
        self.store = store

    def create_case(self, raw_input: str, factory_id: str) -> Case:
        case_id = self._generate_case_id()
        case = Case(
            case_id=case_id,
            status=CaseStatus.D0_D4,
            factory_id=factory_id,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            data_sources=[DataSource(type="cli_input", ref="new", summary=raw_input)],
        )
        case.add_history("new", input_text=raw_input)
        self.store.save_case(case)
        return case

    def get_case(self, case_id: str) -> Case | None:
        return self.store.load_case(case_id)

    def update_answer(
        self,
        case_id: str,
        question_id: str,
        value: Any,
        status: str = "complete",
    ) -> Case:
        case = self.store.load_case(case_id)
        if case is None:
            raise ValueError(f"Case not found: {case_id}")
        case.set_answer(question_id, value, status)
        case.add_history("answer", question_id=question_id, input_text=str(value)[:200])
        self.store.save_case(case)
        return case

    def list_cases(self) -> list[Case]:
        return self.store.load_all_cases()

    def _generate_case_id(self) -> str:
        prefix = "CASE"
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d")
        existing = set(self.store.list_cases())
        counter = 1
        while True:
            candidate = f"{prefix}-{timestamp}-{counter:03d}"
            if candidate not in existing:
                return candidate
            counter += 1
