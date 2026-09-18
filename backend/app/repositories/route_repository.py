from typing import Optional

from sqlalchemy.orm import Session

from app.models.route import Route


class RouteRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, route: Route) -> Route:
        merged = self.session.merge(route)
        self.session.commit()
        return merged

    def find_by_id(self, route_id: int) -> Optional[Route]:
        return self.session.get(Route, route_id)

    def find_all(self) -> list[Route]:
        return self.session.query(Route).all()
