"""Factory experience retrieval and update service."""

from fireline.adapters.storage.json_store import JsonStore
from fireline.domain.models.case import Case
from fireline.domain.models.factory import FactoryExperience, TruthChain


class ExperienceService:
    def __init__(self, store: JsonStore):
        self.store = store

    def get_experience(self) -> FactoryExperience | None:
        return self.store.load_experience()

    def get_context_for_case(self, case: Case) -> FactoryExperience | None:
        """Return a subset of experience relevant to the case."""
        full = self.store.load_experience()
        if not full:
            return None

        search_text = self._case_search_text(case)
        relevant_patterns = self._match_patterns(full, search_text)
        relevant_chains = self._match_truth_chains(full, search_text)

        if not relevant_patterns and full.patterns:
            relevant_patterns = full.patterns[:2]

        return FactoryExperience(
            factory_id=full.factory_id,
            mode=full.mode,
            patterns=relevant_patterns,
            vocabulary=full.vocabulary,
            control_point_map=full.control_point_map,
            truth_chains=relevant_chains,
            updated_at=full.updated_at,
        )

    def _case_search_text(self, case: Case) -> str:
        """Build a lowercase search string from key case answers."""
        parts = []
        for qid in ("d0-q1", "d2-q1", "d4-q2"):
            ans = case.answers.get(qid)
            if ans and ans.value:
                parts.append(str(ans.value))
        return " ".join(parts).lower()

    def _match_patterns(self, experience: FactoryExperience, search_text: str) -> list:
        """Match patterns by phenomenon type or typical causes."""
        scored = []
        for pattern in experience.patterns:
            score = 0
            pt = pattern.phenomenon_type.lower()
            if pt in search_text or search_text in pt:
                score += 2
            for cause in pattern.typical_causes:
                cause_text = str(cause.get("cause", "")).lower()
                if cause_text and (cause_text in search_text or search_text in cause_text):
                    score += 1
            if score > 0:
                scored.append((score, pattern))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [p for _, p in scored[:3]]

    def _match_truth_chains(
        self, experience: FactoryExperience, search_text: str
    ) -> list[TruthChain]:
        """Match truth chains by phenomenon or root cause."""
        matched = []
        for chain in experience.truth_chains:
            phenomenon = chain.phenomenon.lower()
            root_cause = chain.verified_root_cause.lower()
            if (
                phenomenon in search_text
                or search_text in phenomenon
                or root_cause in search_text
                or search_text in root_cause
            ):
                matched.append(chain)
        return matched[:3]

    def ensure_default_experience(self) -> FactoryExperience:
        exp = self.store.load_experience()
        if exp:
            return exp
        exp = FactoryExperience(factory_id=self.store.factory_id)
        self.store.save_experience(exp)
        return exp
