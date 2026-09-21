from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.generation import Generation


class GenerationRepository:

    def create(
        self,
        db: Session,
        generation: Generation
    ) -> Generation:

        db.add(generation)
        db.flush()

        return generation

    def update(
        self,
        db: Session,
        generation: Generation
    ) -> Generation:

        db.add(generation)
        db.flush()

        return generation

    def get_by_id(
        self,
        db: Session,
        generation_id: int
    ) -> Generation | None:

        return db.get(
            Generation,
            generation_id
        )

    def get_all(
        self,
        db: Session
    ) -> list[Generation]:

        result = db.execute(
            select(Generation)
            .order_by(
                Generation.created_at.desc()
            )
        )

        return list(
            result.scalars().all()
        )