import logging
from datetime import datetime, timezone

from app.exceptions import BusinessError
from app.models.questionnaire_answer import QuestionnaireAnswer
from app.repositories.questionnaire_answer_repository import (
    QuestionnaireAnswerRepository,
)
from app.repositories.questionnaire_question_repository import (
    QuestionnaireQuestionRepository,
)

logger = logging.getLogger(__name__)


class QuestionnaireService:
    def __init__(
        self,
        answer_repository: QuestionnaireAnswerRepository,
        question_repository: QuestionnaireQuestionRepository,
    ):
        self.answer_repository = answer_repository
        self.question_repository = question_repository

    def submit_answers(self, user_id: int, answers: list[dict]) -> None:
        submitted = {a["question_code"]: a["answer_value"] for a in answers}

        all_questions = self.question_repository.find_all()
        required_codes = {q.code for q in all_questions if q.is_required}
        code_to_question = {q.code: q for q in all_questions}

        existing_answers = self.answer_repository.find_all_by_user(user_id)
        code_by_question_id = {q.id: q.code for q in all_questions}
        existing_codes = {
            code_by_question_id[a.question_id]
            for a in existing_answers
            if a.question_id in code_by_question_id
        }

        resulting_codes = existing_codes | submitted.keys()
        if not required_codes.issubset(resulting_codes):
            logger.warning(
                "Missing required answers: userId=%s missingCodes=%s",
                user_id,
                sorted(required_codes - resulting_codes),
            )
            raise BusinessError("MISSING_REQUIRED_ANSWER")

        for code, value in submitted.items():
            question = code_to_question.get(code)
            if question is None:
                continue

            existing = self.answer_repository.find_by_user_and_question(
                user_id, question.id
            )
            if existing is not None:
                existing.answer_value = value
                existing.answered_at = datetime.now(timezone.utc)
                self.answer_repository.save(existing)
            else:
                answer = QuestionnaireAnswer(
                    user_id=user_id,
                    question_id=question.id,
                    answer_value=value,
                    answered_at=datetime.now(timezone.utc),
                )
                self.answer_repository.save(answer)

        logger.info(
            "Questionnaire answers submitted: userId=%s answeredCount=%d",
            user_id,
            len(submitted),
        )
