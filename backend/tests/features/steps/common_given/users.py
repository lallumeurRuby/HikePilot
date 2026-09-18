from datetime import datetime, timezone

from behave import given

from app.models.user import User
from app.repositories.user_repository import UserRepository


@given("系統中有以下使用者：")
def step_impl(context):
    db_session = context.db_session
    repository = UserRepository(db_session)

    for row in context.table:
        user = User(
            google_id=row["google_id"],
            email=row["email"],
            name=row["name"],
            created_at=datetime.now(timezone.utc),
        )
        saved = repository.save(user)
        context.ids[row["name"]] = saved.id
