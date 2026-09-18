import jwt

from app.core.config import settings


class JwtHelper:
    SECRET = settings.JWT_SECRET
    ALGORITHM = settings.JWT_ALGORITHM

    def generate_token(self, player_name: str) -> str:
        payload = {"player_name": player_name}
        return jwt.encode(payload, self.SECRET, algorithm=self.ALGORITHM)
