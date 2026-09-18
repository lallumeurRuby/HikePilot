import logging
from datetime import datetime, timezone

from app.exceptions import BusinessError
from app.models.enums import SectionName
from app.models.hiking_plan import HikingPlan
from app.models.hiking_plan_section import HikingPlanSection
from app.repositories.hiking_plan_repository import HikingPlanRepository
from app.repositories.recommendation_repository import RecommendationRepository

SECTION_NAME_LABELS: dict[SectionName, str] = {
    SectionName.ROUTE_SUMMARY: "路線摘要",
    SectionName.ITINERARY: "分段行程",
    SectionName.WEATHER_CONDITIONS: "天氣路況",
    SectionName.RISK_RESPONSE: "風險應對",
    SectionName.GEAR_SUPPLY: "裝備補給",
    SectionName.TRANSPORTATION: "交通資訊",
    SectionName.EMERGENCY_RESPONSE: "緊急應變（撤退條件、替代方案）",
    SectionName.PRE_TRIP_CHECKLIST: "行前 Checklist",
}

SECTION_ORDER = list(SECTION_NAME_LABELS.keys())

logger = logging.getLogger(__name__)


class PlanService:
    def __init__(
        self,
        hiking_plan_repository: HikingPlanRepository,
        recommendation_repository: RecommendationRepository,
    ):
        self.hiking_plan_repository = hiking_plan_repository
        self.recommendation_repository = recommendation_repository

    def generate_plan(self, user_id: int, route_id: int | None) -> dict:
        if route_id is None:
            logger.warning("Route not selected: userId=%s", user_id)
            raise BusinessError("ROUTE_NOT_SELECTED")

        recommendation = self.recommendation_repository.find_latest_by_user(user_id)
        recommended_route_ids = (
            {
                rr.route_id
                for rr in self.recommendation_repository.find_routes(recommendation.id)
            }
            if recommendation is not None
            else set()
        )
        if route_id not in recommended_route_ids:
            logger.warning(
                "Route not in recommendation: userId=%s routeId=%s", user_id, route_id
            )
            raise BusinessError("ROUTE_NOT_IN_RECOMMENDATION")

        plan = HikingPlan(
            user_id=user_id,
            route_id=route_id,
            recommendation_id=recommendation.id,
            pdf_url=f"https://hikepilot.example.com/plans/{user_id}-{route_id}.pdf",
            generated_at=datetime.now(timezone.utc),
        )
        saved_plan = self.hiking_plan_repository.save(plan)

        sections = []
        for order, section_name in enumerate(SECTION_ORDER, start=1):
            self.hiking_plan_repository.save_section(
                HikingPlanSection(
                    hiking_plan_id=saved_plan.id,
                    section_order=order,
                    section_name=section_name,
                )
            )
            sections.append(
                {
                    "section_order": order,
                    "section_name": SECTION_NAME_LABELS[section_name],
                }
            )

        logger.info(
            "Hiking plan generated: userId=%s planId=%s routeId=%s",
            user_id,
            saved_plan.id,
            route_id,
        )

        return {"sections": sections, "pdf_url": saved_plan.pdf_url}
