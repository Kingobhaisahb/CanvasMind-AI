from app.models.painting_type import PaintingType
from app.orchestration.composition_engine import CompositionEngine
from app.orchestration.description_analyzer import DescriptionAnalyzer
from app.orchestration.generation_spec import (
    ColorDirectionSpec,
    CompositionSpec,
    DimensionSpec,
    EnvironmentSpec,
    GenerationSpec,
    LightingSpec,
    StyleSpec,
    SubjectSpec
)
from app.orchestration.style_specialist import StyleSpecialist
from app.schemas.dimension import DimensionRequest
from app.services.dimension_service import DimensionService


class Orchestrator:

    def __init__(self):
        self.style_specialist = StyleSpecialist()
        self.composition_engine = CompositionEngine()
        self.description_analyzer = DescriptionAnalyzer()
        self.dimension_service = DimensionService()

    def create_generation_spec(
        self,
        description: str,
        painting_type: PaintingType,
        dimensions: DimensionRequest
    ) -> GenerationSpec:

        # Step 1: Analyze the user's description
        (
            subject_spec,
            environment_spec,
            lighting_spec,
            color_direction_spec
        ) = self.description_analyzer.analyze(
            description
        )

        # Step 2: Generate painting-type style information
        style_spec = self.style_specialist.create_style_spec(
            painting_type
        )

        # Step 3: Analyze dimensions
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

        # Step 4: Generate composition information
        composition_spec = (
            self.composition_engine.create_composition_spec(
                description=description,
                dimensions=dimension_spec
            )
        )

        # Step 5: Combine everything into the generation specification
        return GenerationSpec(
            description=description,
            subject=subject_spec,
            environment=environment_spec,
            style=style_spec,
            composition=composition_spec,
            dimensions=dimension_spec,
            lighting=lighting_spec,
            color_direction=color_direction_spec
        )