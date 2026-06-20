"""JSON file storage adapter with factory isolation."""

from pathlib import Path

import yaml

from fireline.domain.models.case import Case
from fireline.domain.models.factory import FactoryExperience


class JsonStore:
    """File-based storage per factory.

    Layout:
        {base_dir}/factories/{factory_id}/cases/{case_id}/meta.json
        {base_dir}/factories/{factory_id}/experience/patterns.yaml
    """

    def __init__(self, factory_id: str, base_dir: Path | None = None):
        self.factory_id = factory_id
        self.base_dir = base_dir or Path.home() / ".fireline" / "data"
        self.factory_dir = self.base_dir / "factories" / factory_id

    def _case_path(self, case_id: str) -> Path:
        return self.factory_dir / "cases" / case_id / "meta.json"

    def save_case(self, case: Case) -> None:
        path = self._case_path(case.case_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(case.model_dump_json(indent=2), encoding="utf-8")

    def load_case(self, case_id: str) -> Case | None:
        path = self._case_path(case_id)
        if not path.exists():
            return None
        return Case.model_validate_json(path.read_text(encoding="utf-8"))

    def list_cases(self) -> list[str]:
        cases_dir = self.factory_dir / "cases"
        if not cases_dir.exists():
            return []
        return [d.name for d in cases_dir.iterdir() if d.is_dir()]

    def save_experience(self, experience: FactoryExperience) -> None:
        path = self.factory_dir / "experience" / "patterns.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(experience.model_dump(mode="json")), encoding="utf-8")

    def load_experience(self) -> FactoryExperience | None:
        path = self.factory_dir / "experience" / "patterns.yaml"
        if not path.exists():
            return None
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        return FactoryExperience.model_validate(data)

    def ensure_factory_dir(self) -> None:
        self.factory_dir.mkdir(parents=True, exist_ok=True)
        (self.factory_dir / "cases").mkdir(exist_ok=True)
        (self.factory_dir / "experience").mkdir(exist_ok=True)

    def case_exists(self, case_id: str) -> bool:
        return self._case_path(case_id).exists()

    def load_all_cases(self) -> list[Case]:
        cases = []
        for case_id in self.list_cases():
            case = self.load_case(case_id)
            if case:
                cases.append(case)
        return cases
