from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.painting_type import PaintingType


class PaintingTypeRepository:

    def get_all(self, db: Session) -> list[PaintingType]:
        result = db.execute(
            select(PaintingType)
            .where(PaintingType.is_active.is_(True))
            .order_by(PaintingType.name)
        )

        return list(result.scalars().all())

    def get_by_code(
        self,
        db: Session,
        code: str
    ) -> PaintingType | None:

        result = db.execute(
            select(PaintingType)
            .where(
                PaintingType.code == code,
                PaintingType.is_active.is_(True)
            )
        )

        return result.scalar_one_or_none()