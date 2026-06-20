"""Gate service: stage advancement checks."""

from __future__ import annotations

from eight_d_coach import GateValidator

from fireline.adapters.skill.mapper import map_case_to_skill
from fireline.domain.models.case import Case, CaseStatus


class GateService:
    def __init__(self):
        self.validator = GateValidator()

    def can_advance(self, case: Case, target_status: CaseStatus) -> tuple[bool, list[str]]:
        """Check if the case can advance to target_status."""
        skill_case = map_case_to_skill(case)
        if target_status == CaseStatus.D5_D8:
            blockers = self.get_blockers(case)
            return len(blockers) == 0, blockers
        if target_status == CaseStatus.CLOSED:
            result = self.validator.check(skill_case, "closed")
            return result.passed, result.blockers
        return True, []

    def get_blockers(self, case: Case) -> list[str]:
        """List all current blockers for the investigation phase."""
        skill_case = map_case_to_skill(case)
        blockers = []
        for check in (
            self.validator.check_d1,
            self.validator.check_d2,
            self.validator.check_d3,
            self.validator.check_d4,
        ):
            result = check(skill_case)
            blockers.extend(result.blockers)
        return blockers
