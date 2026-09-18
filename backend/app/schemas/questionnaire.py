from pydantic import BaseModel


class QuestionnaireAnswerItem(BaseModel):
    question_code: str
    answer_value: str


class SubmitQuestionnaireRequest(BaseModel):
    answers: list[QuestionnaireAnswerItem]
