"""D4 analysis service."""

from fireline.adapters.llm.provider import LLMClient
from fireline.domain.models.case import Case
from fireline.domain.models.factory import FactoryExperience
from fireline.domain.services.question_service import QuestionService


class D4AnalysisService:
    """Coordinates D4-Q2/Q3/Q4 analysis."""

    def __init__(self, llm_client: LLMClient):
        self.question_service = QuestionService(llm_client)

    async def analyze(
        self,
        case: Case,
        experience: FactoryExperience | None,
    ) -> dict:
        """Run D4-Q2, Q3, Q4 guidance in sequence."""
        results = {}
        for qid in ["d4-q2", "d4-q3", "d4-q4"]:
            result = await self.question_service.guide(case, qid, experience)
            results[qid] = result
        return results
