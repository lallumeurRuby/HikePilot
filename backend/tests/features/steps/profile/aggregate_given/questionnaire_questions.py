from behave import given

from app.models.enums import AnswerType
from app.models.questionnaire_question import QuestionnaireQuestion
from app.repositories.questionnaire_question_repository import (
    QuestionnaireQuestionRepository,
)

# Q2「開放文字+單選」不在 erm.dbml 的 answer_type_enum（4 值）中，
# 映射為 OPEN_TEXT（主要作答形式為開放文字）；本測試不驗證 answer_type 的值。
ANSWER_TYPE_MAPPING = {
    "單選": AnswerType.SINGLE_CHOICE,
    "複選": AnswerType.MULTI_CHOICE,
    "開放文字": AnswerType.OPEN_TEXT,
    "開放文字+單選": AnswerType.OPEN_TEXT,
    "矩陣單選": AnswerType.MATRIX_SINGLE_CHOICE,
}


@given("個人條件問卷包含以下題項：")
def step_impl(context):
    db_session = context.db_session
    repository = QuestionnaireQuestionRepository(db_session)

    for order, row in enumerate(context.table, start=1):
        question = QuestionnaireQuestion(
            code=row["題號"],
            question_text=row["題目"],
            answer_type=ANSWER_TYPE_MAPPING[row["回答型態"]],
            is_required=(row["是否必答"] == "必答"),
            display_order=order,
        )
        repository.save(question)
