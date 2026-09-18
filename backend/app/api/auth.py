from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import create_access_token, get_db
from app.core.google_oauth import GoogleIdentity, verify_google_id_token
from app.repositories.user_repository import UserRepository
from app.schemas.auth import GoogleLoginRequest
from app.services.auth_service import AuthService

router = APIRouter()


def get_google_identity(request: GoogleLoginRequest) -> GoogleIdentity:
    return verify_google_id_token(request.id_token)


@router.post("/auth/google")
def login_with_google(
    identity: GoogleIdentity = Depends(get_google_identity),
    db: Session = Depends(get_db),
):
    service = AuthService(UserRepository(db))
    user, is_new_user = service.login_with_google(
        identity.google_id, identity.email, identity.name
    )

    data = {"is_new_user": is_new_user, "token": create_access_token(user.id)}
    if is_new_user:
        data["next_step"] = "questionnaire"

    return {"success": True, "data": data}
