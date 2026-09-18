from datetime import datetime, timezone

from behave import given

from app.models.questionnaire_answer import QuestionnaireAnswer
from app.repositories.questionnaire_answer_repository import (
    QuestionnaireAnswerRepository,
)
from app.repositories.questionnaire_question_repository import (
    QuestionnaireQuestionRepository,
)


@given('使用者 "{user_name}" 已回答問卷：')
def step_impl(context, user_name):
    db_session = context.db_session
    answer_repository = QuestionnaireAnswerRepository(db_session)
    question_repository = QuestionnaireQuestionRepository(db_session)

    if user_name not in context.ids:
        raise KeyError(f"找不到使用者 '{user_name}' 的 ID，請先建立使用者")
    user_id = context.ids[user_name]

    for row in context.table:
        question = question_repository.find_by_code(row["question_code"])
        if question is None:
            raise KeyError(f"找不到題項 '{row['question_code']}'")

        answer = QuestionnaireAnswer(
            user_id=user_id,
            question_id=question.id,
            answer_value=row["answer_value"],
            answered_at=datetime.now(timezone.utc),
        )
        answer_repository.save(answer)
