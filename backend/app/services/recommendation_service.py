import logging
from datetime import datetime, timezone

from app.exceptions import BusinessError
from app.models.recommendation import Recommendation
from app.models.recommendation_route import RecommendationRoute
from app.repositories.questionnaire_answer_repository import (
    QuestionnaireAnswerRepository,
)
from app.repositories.questionnaire_question_repository import (
    QuestionnaireQuestionRepository,
)
from app.repositories.recommendation_repository import RecommendationRepository
from app.repositories.route_repository import RouteRepository

logger = logging.getLogger(__name__)

MAX_RECOMMENDED_ROUTES = 3


class RecommendationService:
    def __init__(
        self,
        recommendation_repository: RecommendationRepository,
        route_repository: RouteRepository,
        answer_repository: QuestionnaireAnswerRepository,
        question_repository: QuestionnaireQuestionRepository,
    ):
        self.recommendation_repository = recommendation_repository
        self.route_repository = route_repository
        self.answer_repository = answer_repository
        self.question_repository = question_repository

    def request_recommendation(self, user_id: int) -> dict:
        self._ensure_profile_complete(user_id)

        candidate_routes = self.route_repository.find_all()
        matched_routes = candidate_routes[:MAX_RECOMMENDED_ROUTES]

        recommendation = Recommendation(
            user_id=user_id,
            requested_at=datetime.now(timezone.utc),
            has_matches=len(matched_routes) > 0,
        )
        saved_recommendation = self.recommendation_repository.save(recommendation)

        for rank, route in enumerate(matched_routes, start=1):
            self.recommendation_repository.save_route(
                RecommendationRoute(
                    recommendation_id=saved_recommendation.id,
                    route_id=route.id,
                    rank=rank,
                )
            )

        logger.info(
            "Recommendation created: userId=%s recommendationId=%s routeCount=%d",
            user_id,
            saved_recommendation.id,
            len(matched_routes),
        )

        return {
            "has_matches": saved_recommendation.has_matches,
            "routes": [
                {"route_id": route.id, "name": route.name} for route in matched_routes
            ],
        }

    def _ensure_profile_complete(self, user_id: int) -> None:
        all_questions = self.question_repository.find_all()
        required_codes = {q.code for q in all_questions if q.is_required}

        answers = self.answer_repository.find_all_by_user(user_id)
        code_by_question_id = {q.id: q.code for q in all_questions}
        answered_codes = {
            code_by_question_id[a.question_id]
            for a in answers
            if a.question_id in code_by_question_id
        }

        if not required_codes.issubset(answered_codes):
            logger.warning("Profile incomplete: userId=%s", user_id)
            raise BusinessError("PROFILE_INCOMPLETE")
