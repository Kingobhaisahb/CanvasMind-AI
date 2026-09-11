from fastapi import APIRouter

from app.schemas.dimension import (
    DimensionRequest,
    DimensionResponse
)
from app.services.dimension_service import DimensionService


router = APIRouter(
    prefix="/dimensions",
    tags=["Dimensions"]
)

dimension_service = DimensionService()


@router.post(
    "",
    response_model=DimensionResponse
)
def calculate_dimensions(
    dimensions: DimensionRequest
):
    return dimension_service.calculate(dimensions)