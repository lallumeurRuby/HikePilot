from pydantic import BaseModel


class GeneratePlanRequest(BaseModel):
    route_id: int | None = None
