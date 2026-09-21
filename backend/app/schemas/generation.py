from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class GenerationRequest(BaseModel):

    description: str = Field(
        min_length=1,
        max_length=5000
    )

    painting_type: str = Field(
        min_length=1,
        max_length=50
    )

    width: float = Field(
        gt=0
    )

    height: float = Field(
        gt=0
    )

    unit: str = Field(
        default="px",
        min_length=1,
        max_length=20
    )


class GenerationResponse(BaseModel):

    id: int

    description: str

    painting_type: str

    width: float
    height: float
    unit: str

    aspect_ratio: float
    orientation: str

    prompt: str

    provider: str | None
    model: str | None

    image_path: str | None

    status: str

    error_message: str | None

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )