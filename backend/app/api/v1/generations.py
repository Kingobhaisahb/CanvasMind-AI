from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.providers.image_generation_provider import (
    HuggingFaceImageGenerationProvider
)
from app.schemas.dimension import DimensionRequest
from app.schemas.generation import (
    GenerationRequest,
    GenerationResponse
)
from app.services.generation_service import GenerationService
from app.services.painting_type_service import (
    PaintingTypeService
)
from app.storage.image_storage import ImageStorage


router = APIRouter(
    prefix="/generations",
    tags=["Generations"]
)


painting_type_service = PaintingTypeService()

generation_service = GenerationService(
    provider=HuggingFaceImageGenerationProvider(),
    storage=ImageStorage()
)


@router.post(
    "",
    response_model=GenerationResponse
)
def create_generation(
    request: GenerationRequest,
    db: Session = Depends(get_db)
):

    # ----------------------------------------
    # Find requested painting type
    # ----------------------------------------

    painting_type = (
        painting_type_service.get_by_code(
            db,
            request.painting_type
        )
    )

    if painting_type is None:

        raise HTTPException(
            status_code=404,
            detail="Painting type not found"
        )

    # ----------------------------------------
    # Build dimensions
    # ----------------------------------------

    dimensions = DimensionRequest(
        width=request.width,
        height=request.height,
        unit=request.unit
    )

    # ----------------------------------------
    # Generate artwork
    # ----------------------------------------

    try:

        generation = generation_service.generate(
            db=db,
            description=request.description,
            painting_type=painting_type,
            dimensions=dimensions
        )

        return generation

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Image generation failed"
        )


@router.get(
    "/{generation_id}",
    response_model=GenerationResponse
)
def get_generation(
    generation_id: int,
    db: Session = Depends(get_db)
):

    generation = generation_service.repository.get_by_id(
        db,
        generation_id
    )

    if generation is None:

        raise HTTPException(
            status_code=404,
            detail="Generation not found"
        )

    return generation


@router.get(
    "",
    response_model=list[GenerationResponse]
)
def get_generations(
    db: Session = Depends(get_db)
):

    return generation_service.repository.get_all(
        db
    )