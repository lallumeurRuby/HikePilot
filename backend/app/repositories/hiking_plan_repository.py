from typing import Optional

from sqlalchemy.orm import Session

from app.models.hiking_plan import HikingPlan
from app.models.hiking_plan_section import HikingPlanSection


class HikingPlanRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, plan: HikingPlan) -> HikingPlan:
        merged = self.session.merge(plan)
        self.session.commit()
        return merged

    def save_section(self, section: HikingPlanSection) -> HikingPlanSection:
        merged = self.session.merge(section)
        self.session.commit()
        return merged

    def find_by_id(self, plan_id: int) -> Optional[HikingPlan]:
        return self.session.get(HikingPlan, plan_id)

    def find_sections(self, plan_id: int) -> list[HikingPlanSection]:
        return (
            self.session.query(HikingPlanSection)
            .filter_by(hiking_plan_id=plan_id)
            .order_by(HikingPlanSection.section_order)
            .all()
        )
