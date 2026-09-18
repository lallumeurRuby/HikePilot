from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.models.hiking_plan import HikingPlan  # noqa: E402
from app.models.hiking_plan_section import HikingPlanSection  # noqa: E402
from app.models.questionnaire_answer import QuestionnaireAnswer  # noqa: E402
from app.models.questionnaire_question import QuestionnaireQuestion  # noqa: E402
from app.models.recommendation import Recommendation  # noqa: E402
from app.models.recommendation_route import RecommendationRoute  # noqa: E402
from app.models.route import Route  # noqa: E402
from app.models.user import User  # noqa: E402

__all__ = [
    "Base",
    "User",
    "QuestionnaireQuestion",
    "QuestionnaireAnswer",
    "Route",
    "Recommendation",
    "RecommendationRoute",
    "HikingPlan",
    "HikingPlanSection",
]
