from datetime import datetime, timezone

from behave import given

from app.models.enums import OpenStatus
from app.models.recommendation import Recommendation
from app.models.recommendation_route import RecommendationRoute
from app.models.route import Route
from app.repositories.recommendation_repository import RecommendationRepository
from app.repositories.route_repository import RouteRepository


@given("使用者已取得路線推薦結果")
def step_impl_background(context):
    # Background 描述性語句，不對應具體 Aggregate 寫入。
    pass


@given('使用者 "{user_name}" 已取得以下路線推薦結果：')
def step_impl(context, user_name):
    db_session = context.db_session
    route_repository = RouteRepository(db_session)
    recommendation_repository = RecommendationRepository(db_session)

    if user_name not in context.ids:
        raise KeyError(f"找不到使用者 '{user_name}' 的 ID，請先建立使用者")
    user_id = context.ids[user_name]

    recommendation = Recommendation(
        user_id=user_id,
        requested_at=datetime.now(timezone.utc),
        has_matches=True,
    )
    saved_recommendation = recommendation_repository.save(recommendation)
    context.memo["last_recommendation_id"] = saved_recommendation.id

    for rank, row in enumerate(context.table, start=1):
        route = Route(name=row["name"], open_status=OpenStatus.OPEN)
        saved_route = route_repository.save(route)
        context.ids[row["route_id"]] = saved_route.id

        recommendation_route = RecommendationRoute(
            recommendation_id=saved_recommendation.id,
            route_id=saved_route.id,
            rank=rank,
        )
        recommendation_repository.save_route(recommendation_route)
