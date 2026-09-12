from app.orchestration.style_specialist import StyleSpecialist
from app.models.painting_type import PaintingType
from app.orchestration.composition_engine import CompositionEngine
from app.orchestration.generation_spec import DimensionSpec
from app.orchestration.orchestrator import Orchestrator
from app.schemas.dimension import DimensionRequest




def test_style_specialist():

    painting_type = PaintingType(
        code="MADHUBANI",
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


from app.orchestration.prompt_compiler import PromptCompiler
from app.orchestration.generation_spec import (
    GenerationSpec,
    StyleSpec,
    DimensionSpec,
    CompositionSpec
)


def test_prompt_compiler():

    generation_spec = GenerationSpec(
        description="A woman walking through a village",

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
            negative_constraints=[
                "photorealistic"
            ]
        ),

        dimensions=DimensionSpec(
            width=1920,
            height=1080,
            unit="px",
            aspect_ratio=1.7778,
            orientation="landscape"
        ),

        composition=CompositionSpec(
            subject_placement="Place the primary subject slightly off-center.",
            framing="Use wide framing.",
            negative_space="Maintain moderate negative space.",
            balance="Balance supporting elements horizontally."
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

