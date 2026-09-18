from sqlalchemy.orm import Session

from app.models.questionnaire_question_option import QuestionnaireQuestionOption


class QuestionnaireQuestionOptionRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, option: QuestionnaireQuestionOption) -> QuestionnaireQuestionOption:
        merged = self.session.merge(option)
        self.session.commit()
        return merged

    def find_all(self) -> list[QuestionnaireQuestionOption]:
        return (
            self.session.query(QuestionnaireQuestionOption)
            .order_by(QuestionnaireQuestionOption.display_order)
            .all()
        )

    def find_by_question_code(
        self, question_code: str
    ) -> list[QuestionnaireQuestionOption]:
        return (
            self.session.query(QuestionnaireQuestionOption)
            .filter_by(question_code=question_code)
            .order_by(QuestionnaireQuestionOption.display_order)
            .all()
        )
