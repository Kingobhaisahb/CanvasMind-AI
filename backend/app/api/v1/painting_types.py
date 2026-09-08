from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.painting_type import PaintingTypeResponse
from app.services.painting_type_service import PaintingTypeService


router = APIRouter(
    prefix="/painting-types",
    tags=["Painting Types"]
)

painting_type_service = PaintingTypeService()


@router.get(
    "",
    response_model=list[PaintingTypeResponse]
)
def get_painting_types(
    db: Session = Depends(get_db)
):
    return painting_type_service.get_all(db)


@router.get(
    "/{code}",
    response_model=PaintingTypeResponse
)
def get_painting_type(
    code: str,
    db: Session = Depends(get_db)
):
    painting_type = painting_type_service.get_by_code(
        db,
        code
    )

    if painting_type is None:
        raise HTTPException(
            status_code=404,
            detail="Painting type not found"
        )

    return painting_type