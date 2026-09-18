from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user_id, get_db
from app.repositories.questionnaire_answer_repository import (
    QuestionnaireAnswerRepository,
)
from app.repositories.questionnaire_question_repository import (
    QuestionnaireQuestionRepository,
)
from app.schemas.questionnaire import SubmitQuestionnaireRequest
from app.services.questionnaire_service import QuestionnaireService

router = APIRouter()


@router.post("/profile/questionnaire")
def submit_questionnaire(
    request: SubmitQuestionnaireRequest,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    service = QuestionnaireService(
        QuestionnaireAnswerRepository(db), QuestionnaireQuestionRepository(db)
    )
    service.submit_answers(user_id, [a.model_dump() for a in request.answers])
    return {"success": True}
