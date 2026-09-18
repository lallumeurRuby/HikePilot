from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import create_access_token, get_db
from app.repositories.user_repository import UserRepository
from app.schemas.auth import GoogleLoginRequest
from app.services.auth_service import AuthService

router = APIRouter()


@router.post("/auth/google")
def login_with_google(request: GoogleLoginRequest, db: Session = Depends(get_db)):
    service = AuthService(UserRepository(db))
    user, is_new_user = service.login_with_google(
        request.google_id, request.email, request.name
    )

    data = {"is_new_user": is_new_user, "token": create_access_token(user.id)}
    if is_new_user:
        data["next_step"] = "questionnaire"

    return {"success": True, "data": data}
