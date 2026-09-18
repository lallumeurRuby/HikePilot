from fastapi import APIRouter

from app.api.auth import router as auth_router
from app.api.plan import router as plan_router
from app.api.profile import router as profile_router
from app.api.recommendation import router as recommendation_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(profile_router)
router.include_router(recommendation_router)
router.include_router(plan_router)
