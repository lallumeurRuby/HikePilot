from dataclasses import dataclass

from google.auth.transport import requests as google_requests
from google.oauth2 import id_token as google_id_token

from app.core.config import settings
from app.exceptions import BusinessError


@dataclass(frozen=True)
class GoogleIdentity:
    google_id: str
    email: str
    name: str


def verify_google_id_token(token: str) -> GoogleIdentity:
    """Verify a Google-issued ID token's signature, issuer, audience and expiry.

    Only claims from the verified payload are trusted — never caller-supplied
    google_id/email/name.
    """
    try:
        payload = google_id_token.verify_oauth2_token(
            token, google_requests.Request(), settings.GOOGLE_CLIENT_ID
        )
    except ValueError as exc:
        raise BusinessError("INVALID_GOOGLE_TOKEN") from exc

    sub = payload.get("sub")
    email = payload.get("email")
    if not sub or not email:
        raise BusinessError("INVALID_GOOGLE_TOKEN")

    return GoogleIdentity(google_id=sub, email=email, name=payload.get("name", ""))
