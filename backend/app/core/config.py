import os


class Settings:
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://postgres:postgres@localhost:5433/hikepilot_backend_dev",
    )
    API_PREFIX: str = "/api"

    # Auth
    JWT_SECRET: str = os.getenv("JWT_SECRET", "test-secret-key")
    JWT_ALGORITHM: str = "HS256"

    # Google OAuth（audience，必須與 GCP 建立的 OAuth Client ID 一致）
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID", "")


settings = Settings()
