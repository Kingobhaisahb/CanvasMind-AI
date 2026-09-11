from app.schemas.dimension import (
    DimensionRequest,
    DimensionResponse
)


class DimensionService:

    def calculate(
        self,
        dimensions: DimensionRequest
    ) -> DimensionResponse:

        aspect_ratio = dimensions.width / dimensions.height

        if aspect_ratio > 1:
            orientation = "landscape"
        elif aspect_ratio < 1:
            orientation = "portrait"
        else:
            orientation = "square"

        return DimensionResponse(
            width=dimensions.width,
            height=dimensions.height,
            unit=dimensions.unit,
            aspect_ratio=round(aspect_ratio, 4),
            orientation=orientation
        )