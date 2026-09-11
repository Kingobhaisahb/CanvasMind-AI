from pydantic import BaseModel, Field


class DimensionRequest(BaseModel):
    width: float = Field(gt=0)
    height: float = Field(gt=0)
    unit: str = "px"


class DimensionResponse(BaseModel):
    width: float
    height: float
    unit: str
    aspect_ratio: float
    orientation: str