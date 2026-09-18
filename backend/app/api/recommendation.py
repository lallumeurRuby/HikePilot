from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user_id, get_db
from app.repositories.questionnaire_answer_repository import (
    QuestionnaireAnswerRepository,
)
from app.repositories.questionnaire_question_repository import (
    QuestionnaireQuestionRepository,
)
from app.repositories.recommendation_repository import RecommendationRepository
from app.repositories.route_repository import RouteRepository
from app.services.recommendation_service import RecommendationService

router = APIRouter()


@router.post("/recommendations")
def request_recommendation(
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    service = RecommendationService(
        RecommendationRepository(db),
        RouteRepository(db),
        QuestionnaireAnswerRepository(db),
        QuestionnaireQuestionRepository(db),
    )
    data = service.request_recommendation(user_id)
    return {"success": True, "data": data}
