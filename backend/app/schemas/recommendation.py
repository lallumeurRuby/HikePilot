from pydantic import BaseModel


class RouteSummary(BaseModel):
    route_id: int
    name: str
