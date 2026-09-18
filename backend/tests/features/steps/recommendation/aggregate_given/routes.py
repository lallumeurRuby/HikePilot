from behave import given

from app.models.enums import DifficultyLevel, OpenStatus
from app.models.route import Route
from app.repositories.route_repository import RouteRepository


@given("系統中有以下路線：")
def step_impl(context):
    db_session = context.db_session
    repository = RouteRepository(db_session)

    for row in context.table:
        route = Route(
            name=row["name"],
            region=row.get("region") or None,
            difficulty_level=(
                DifficultyLevel(row["difficulty_level"])
                if row.get("difficulty_level")
                else None
            ),
            open_status=OpenStatus(row["open_status"]),
        )
        saved = repository.save(route)
        context.ids[row["route_id"]] = saved.id
