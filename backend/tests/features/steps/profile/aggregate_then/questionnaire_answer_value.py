from behave import then

from app.repositories.questionnaire_answer_repository import (
    QuestionnaireAnswerRepository,
)
from app.repositories.questionnaire_question_repository import (
    QuestionnaireQuestionRepository,
)


@then('使用者 "{user_name}" 的問卷回答 "{question_code}" 應為 "{answer_value}"')
def step_impl(context, user_name, question_code, answer_value):
    db_session = context.db_session
    answer_repository = QuestionnaireAnswerRepository(db_session)
    question_repository = QuestionnaireQuestionRepository(db_session)

    if user_name not in context.ids:
        raise KeyError(f"找不到使用者 '{user_name}' 的 ID")
    user_id = context.ids[user_name]

    question = question_repository.find_by_code(question_code)
    assert question is not None, f"找不到題項 '{question_code}'"

    answer = answer_repository.find_by_user_and_question(user_id, question.id)
    assert answer is not None, f"找不到使用者 '{user_name}' 對 '{question_code}' 的回答"
    assert (
        answer.answer_value == answer_value
    ), f"預期回答 '{answer_value}'，實際 '{answer.answer_value}'"
