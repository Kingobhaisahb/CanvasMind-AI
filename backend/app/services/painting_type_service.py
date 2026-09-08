from sqlalchemy.orm import Session

from app.repositories.painting_type_repository import PaintingTypeRepository


class PaintingTypeService:

    def __init__(self):
        self.repository = PaintingTypeRepository()

    def get_all(self, db: Session):
        return self.repository.get_all(db)

    def get_by_code(
        self,
        db: Session,
        code: str
    ):
        return self.repository.get_by_code(db, code)