from app.models.painting_type import PaintingType
from app.providers.image_generation_provider import (
    HuggingFaceImageGenerationProvider
)
from app.schemas.dimension import DimensionRequest
from app.services.generation_service import GenerationService


painting_type = PaintingType(
    code="madhubani",
    name="Madhubani",
    description="Traditional Indian folk painting",
    configuration={
        "visual_characteristics": [
            "intricate traditional folk-art patterns",
            "decorative flat composition",
            "ornamental detailing"
        ],
        "color_tendencies": [
            "vivid red",
            "yellow",
            "green",
            "black outlines"
        ],
        "texture_characteristics": [
            "hand-painted paper texture"
        ],
        "line_characteristics": [
            "bold black contour lines",
            "fine decorative patterns"
        ],
        "negative_constraints": [
            "photorealism",
            "3D rendering",
            "modern digital painting"
        ]
    }
)


provider = HuggingFaceImageGenerationProvider()

generation_service = GenerationService(
    provider=provider
)


result = generation_service.generate(
    description=(
        "A peaceful village scene with trees, birds, "
        "a small pond, and traditional houses"
    ),
    painting_type=painting_type,
    dimensions=DimensionRequest(
        width=1024,
        height=1024,
        unit="px"
    )
)


print("IMAGE GENERATION SUCCESSFUL")
print("Provider:", result.provider_name)
print("Metadata:", result.metadata)