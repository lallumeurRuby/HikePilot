from pydantic import BaseModel


class GoogleLoginRequest(BaseModel):
    google_id: str
    email: str
    name: str
