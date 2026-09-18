from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api import router as api_router
from app.core.config import settings
from app.core.deps import set_session_factory
from app.core.logging_config import setup_logging
from app.exceptions import BusinessError, NotFoundError

setup_logging()

VIOLATION_STATUS_CODES = {
    "UNAUTHENTICATED": 401,
    "MISSING_REQUIRED_ANSWER": 400,
    "PROFILE_INCOMPLETE": 422,
    "ROUTE_NOT_SELECTED": 400,
    "ROUTE_NOT_IN_RECOMMENDATION": 422,
}


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(settings.DATABASE_URL)
    set_session_factory(sessionmaker(bind=engine))
    yield
    engine.dispose()


def create_app() -> FastAPI:
    app = FastAPI(title="hikepilot-backend API", version="1.0.0", lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix="/api")

    @app.exception_handler(BusinessError)
    def handle_business_error(request: Request, exc: BusinessError):
        status_code = VIOLATION_STATUS_CODES.get(exc.violation_type, 400)
        return JSONResponse(
            status_code=status_code,
            content={
                "success": False,
                "error": {"violation_type": exc.violation_type},
            },
        )

    @app.exception_handler(NotFoundError)
    def handle_not_found_error(request: Request, exc: NotFoundError):
        return JSONResponse(
            status_code=404,
            content={"success": False, "error": {"message": exc.message}},
        )

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


app = create_app()
