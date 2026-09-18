from behave import given

from app.models.enums import AnswerType
from app.models.questionnaire_question import QuestionnaireQuestion
from app.models.questionnaire_question_option import QuestionnaireQuestionOption
from app.models.questionnaire_question_scenario import QuestionnaireQuestionScenario
from app.repositories.questionnaire_question_option_repository import (
    QuestionnaireQuestionOptionRepository,
)
from app.repositories.questionnaire_question_repository import (
    QuestionnaireQuestionRepository,
)
from app.repositories.questionnaire_question_scenario_repository import (
    QuestionnaireQuestionScenarioRepository,
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


def _parse_code_text_pairs(segment: str) -> list[tuple[str, str]]:
    pairs = []
    for item in segment.split(","):
        item = item.strip()
        if not item or ":" not in item:
            continue
        code, text = item.split(":", 1)
        pairs.append((code.strip(), text.strip()))
    return pairs


@given("個人條件問卷包含以下題項：")
def step_impl(context):
    db_session = context.db_session
    question_repository = QuestionnaireQuestionRepository(db_session)
    option_repository = QuestionnaireQuestionOptionRepository(db_session)
    scenario_repository = QuestionnaireQuestionScenarioRepository(db_session)

    has_options_column = "選項（代碼:文字）" in context.table.headings

    for order, row in enumerate(context.table, start=1):
        code = row["題號"]
        question = QuestionnaireQuestion(
            code=code,
            question_text=row["題目"],
            answer_type=ANSWER_TYPE_MAPPING[row["回答型態"]],
            is_required=(row["是否必答"] == "必答"),
            display_order=order,
        )
        question_repository.save(question)

        if not has_options_column:
            continue

        options_cell = row["選項（代碼:文字）"].strip()
        if options_cell in ("", "（無）"):
            continue

        if "情境（列）" in options_cell:
            scenario_segment, _, level_segment = options_cell.partition("；")
            scenario_segment = scenario_segment.split("：", 1)[-1]
            level_segment = level_segment.split("：", 1)[-1]
            for i, (scenario_code, scenario_text) in enumerate(
                _parse_code_text_pairs(scenario_segment), start=1
            ):
                scenario_repository.save(
                    QuestionnaireQuestionScenario(
                        question_code=code,
                        scenario_code=scenario_code,
                        scenario_text=scenario_text,
                        display_order=i,
                    )
                )
            for i, (option_code, option_text) in enumerate(
                _parse_code_text_pairs(level_segment), start=1
            ):
                option_repository.save(
                    QuestionnaireQuestionOption(
                        question_code=code,
                        option_code=option_code,
                        option_text=option_text,
                        display_order=i,
                    )
                )
        else:
            for i, (option_code, option_text) in enumerate(
                _parse_code_text_pairs(options_cell), start=1
            ):
                option_repository.save(
                    QuestionnaireQuestionOption(
                        question_code=code,
                        option_code=option_code,
                        option_text=option_text,
                        display_order=i,
                    )
                )
