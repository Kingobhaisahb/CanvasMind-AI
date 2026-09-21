from app.models.painting_type import PaintingType
from app.orchestration.composition_engine import CompositionEngine
from app.orchestration.generation_spec import (
    ColorDirectionSpec,
    CompositionSpec,
    DimensionSpec,
    EnvironmentSpec,
    GenerationSpec,
    LightingSpec,
    StyleSpec,
    SubjectSpec,
)
from app.orchestration.orchestrator import Orchestrator
from app.orchestration.prompt_compiler import PromptCompiler
from app.orchestration.style_specialist import StyleSpecialist
from app.schemas.dimension import DimensionRequest


def test_style_specialist():

    painting_type = PaintingType(
        code="MADHUBHANI",
        name="Madhubani",
        description="Traditional Indian folk painting",
        configuration={
            "visual_characteristics": [
                "decorative",
                "highly detailed"
            ],
            "color_tendencies": [
                "vibrant"
            ],
            "texture_characteristics": [
                "hand-painted"
            ],
            "line_characteristics": [
                "strong outlines"
            ],
            "brush_characteristics": [
                "fine controlled strokes"
            ],
            "composition_tendencies": [
                "dense decorative framing"
            ],
            "negative_constraints": [
                "photorealistic"
            ]
        },
        is_active=True
    )

    specialist = StyleSpecialist()

    result = specialist.create_style_spec(
        painting_type
    )

    assert result.painting_type == "Madhubani"
    assert "decorative" in result.visual_characteristics
    assert "vibrant" in result.color_tendencies
    assert "strong outlines" in result.line_characteristics


def test_composition_engine_landscape():

    dimensions = DimensionSpec(
        width=1920,
        height=1080,
        unit="px",
        aspect_ratio=1.7778,
        orientation="landscape"
    )

    engine = CompositionEngine()

    result = engine.create_composition_spec(
        description="A woman walking through a village",
        dimensions=dimensions
    )

    assert result.framing != ""
    assert result.subject_placement != ""
    assert result.negative_space != ""
    assert result.balance != ""


def test_orchestrator():

    painting_type = PaintingType(
        code="MADHUBHANI",
        name="Madhubani",
        description="Traditional Indian folk painting",
        configuration={
            "visual_characteristics": [
                "decorative",
                "highly detailed"
            ],
            "color_tendencies": [
                "vibrant"
            ],
            "texture_characteristics": [
                "hand-painted"
            ],
            "line_characteristics": [
                "strong outlines"
            ],
            "brush_characteristics": [
                "fine controlled strokes"
            ],
            "composition_tendencies": [
                "dense decorative framing"
            ],
            "negative_constraints": [
                "photorealistic"
            ]
        },
        is_active=True
    )

    dimensions = DimensionRequest(
        width=1920,
        height=1080,
        unit="px"
    )

    orchestrator = Orchestrator()

    # Replace the real LLM analyzer with a deterministic fake.
    class FakeDescriptionAnalyzer:

        def analyze(self, description):

            return (
                SubjectSpec(
                    primary_subject="A woman",
                    secondary_subjects=["village"],
                    subject_relationships=[
                        "woman walking through village"
                    ]
                ),
                EnvironmentSpec(
                    setting="village",
                    background_elements=[],
                    depth_elements=[]
                ),
                LightingSpec(
                    lighting_condition="unspecified",
                    light_direction="unspecified",
                    light_quality="unspecified"
                ),
                ColorDirectionSpec(
                    palette=[],
                    contrast="unspecified",
                    saturation="unspecified"
                )
            )

    orchestrator.description_analyzer = FakeDescriptionAnalyzer()

    result = orchestrator.create_generation_spec(
        description="A woman walking through a village",
        painting_type=painting_type,
        dimensions=dimensions
    )

    assert result.description == (
        "A woman walking through a village"
    )

    assert result.style.painting_type == "Madhubani"

    assert result.dimensions.orientation == "landscape"

    assert result.composition.framing != ""

    assert result.subject.primary_subject == "A woman"

    assert "village" in result.subject.secondary_subjects

    assert result.environment.setting == "village"

    assert result.lighting.lighting_condition == "unspecified"

    assert result.color_direction.palette == []


def test_prompt_compiler():

    generation_spec = GenerationSpec(
        description="A woman walking through a village",

        subject=SubjectSpec(
            primary_subject="A woman",
            secondary_subjects=["village"],
            subject_relationships=[
                "woman walking through village"
            ]
        ),

        environment=EnvironmentSpec(
            setting="village",
            background_elements=[],
            depth_elements=[]
        ),

        style=StyleSpec(
            painting_type="Madhubani",
            visual_characteristics=[
                "decorative",
                "highly detailed"
            ],
            color_tendencies=[
                "vibrant"
            ],
            texture_characteristics=[
                "hand-painted"
            ],
            line_characteristics=[
                "strong outlines"
            ],
            brush_characteristics=[
                "fine controlled strokes"
            ],
            composition_tendencies=[
                "dense decorative framing"
            ],
            negative_constraints=[
                "photorealistic"
            ]
        ),

        composition=CompositionSpec(
            subject_placement=(
                "Place the primary subject slightly off-center."
            ),
            framing="Use wide framing.",
            negative_space=(
                "Maintain moderate negative space."
            ),
            balance=(
                "Balance supporting elements horizontally."
            )
        ),

        dimensions=DimensionSpec(
            width=1920,
            height=1080,
            unit="px",
            aspect_ratio=1.7778,
            orientation="landscape"
        ),

        lighting=LightingSpec(
            lighting_condition="natural daylight",
            light_direction="ambient",
            light_quality="soft natural light"
        ),

        color_direction=ColorDirectionSpec(
            palette=["vibrant"],
            contrast="moderate",
            saturation="vibrant"
        )
    )

    compiler = PromptCompiler()

    prompt = compiler.compile(
        generation_spec
    )

    assert "Madhubani" in prompt
    assert "woman walking through a village" in prompt
    assert "vibrant" in prompt
    assert "strong outlines" in prompt
    assert "landscape" in prompt
    assert "photorealistic" in prompt