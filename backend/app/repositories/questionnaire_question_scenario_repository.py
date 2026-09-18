from sqlalchemy.orm import Session

from app.models.questionnaire_question_scenario import QuestionnaireQuestionScenario


class QuestionnaireQuestionScenarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(
        self, scenario: QuestionnaireQuestionScenario
    ) -> QuestionnaireQuestionScenario:
        merged = self.session.merge(scenario)
        self.session.commit()
        return merged

    def find_all(self) -> list[QuestionnaireQuestionScenario]:
        return (
            self.session.query(QuestionnaireQuestionScenario)
            .order_by(QuestionnaireQuestionScenario.display_order)
            .all()
        )

    def find_by_question_code(
        self, question_code: str
    ) -> list[QuestionnaireQuestionScenario]:
        return (
            self.session.query(QuestionnaireQuestionScenario)
            .filter_by(question_code=question_code)
            .order_by(QuestionnaireQuestionScenario.display_order)
            .all()
        )
