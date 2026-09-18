from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user_id, get_db
from app.repositories.hiking_plan_repository import HikingPlanRepository
from app.repositories.recommendation_repository import RecommendationRepository
from app.schemas.plan import GeneratePlanRequest
from app.services.plan_service import PlanService

router = APIRouter()


@router.post("/plans")
def generate_plan(
    request: GeneratePlanRequest,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    service = PlanService(HikingPlanRepository(db), RecommendationRepository(db))
    data = service.generate_plan(user_id, request.route_id)
    return {"success": True, "data": data}
