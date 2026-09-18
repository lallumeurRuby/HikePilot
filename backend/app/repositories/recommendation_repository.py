from typing import Optional

from sqlalchemy.orm import Session

from app.models.recommendation import Recommendation
from app.models.recommendation_route import RecommendationRoute


class RecommendationRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, recommendation: Recommendation) -> Recommendation:
        merged = self.session.merge(recommendation)
        self.session.commit()
        return merged

    def save_route(
        self, recommendation_route: RecommendationRoute
    ) -> RecommendationRoute:
        merged = self.session.merge(recommendation_route)
        self.session.commit()
        return merged

    def find_by_id(self, recommendation_id: int) -> Optional[Recommendation]:
        return self.session.get(Recommendation, recommendation_id)

    def find_latest_by_user(self, user_id: int) -> Optional[Recommendation]:
        return (
            self.session.query(Recommendation)
            .filter_by(user_id=user_id)
            .order_by(Recommendation.requested_at.desc())
            .first()
        )

    def find_routes(self, recommendation_id: int) -> list[RecommendationRoute]:
        return (
            self.session.query(RecommendationRoute)
            .filter_by(recommendation_id=recommendation_id)
            .order_by(RecommendationRoute.rank)
            .all()
        )
