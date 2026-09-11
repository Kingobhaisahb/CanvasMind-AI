from app.models.painting_type import PaintingType
from app.orchestration.composition_engine import CompositionEngine
from app.orchestration.generation_spec import (
    GenerationSpec,
    DimensionSpec
)
from app.orchestration.style_specialist import StyleSpecialist
from app.schemas.dimension import DimensionRequest
from app.services.dimension_service import DimensionService


class Orchestrator:

    def __init__(self):
        self.style_specialist = StyleSpecialist()
        self.composition_engine = CompositionEngine()
        self.dimension_service = DimensionService()

    def create_generation_spec(
        self,
        description: str,
        painting_type: PaintingType,
        dimensions: DimensionRequest
    ) -> GenerationSpec:

        # Step 1: Generate style information
        style_spec = self.style_specialist.create_style_spec(
            painting_type
        )

        # Step 2: Analyze dimensions
        dimension_response = self.dimension_service.calculate(
            dimensions
        )

        dimension_spec = DimensionSpec(
            width=dimension_response.width,
            height=dimension_response.height,
            unit=dimension_response.unit,
            aspect_ratio=dimension_response.aspect_ratio,
            orientation=dimension_response.orientation
        )

        # Step 3: Generate composition information
        composition_spec = (
            self.composition_engine.create_composition_spec(
                description=description,
                dimensions=dimension_spec
            )
        )

        # Step 4: Combine everything
        return GenerationSpec(
            description=description,
            style=style_spec,
            dimensions=dimension_spec,
            composition=composition_spec
        )