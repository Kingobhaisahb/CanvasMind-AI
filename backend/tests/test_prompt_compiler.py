from app.models.painting_type import PaintingType
from app.orchestration.generation_spec import (
    ColorDirectionSpec,
    EnvironmentSpec,
    LightingSpec,
    SubjectSpec,
)
from app.orchestration.orchestrator import Orchestrator
from app.orchestration.prompt_compiler import PromptCompiler
from app.schemas.dimension import DimensionRequest


def make_painting_type(
    code: str,
    name: str,
    configuration: dict
) -> PaintingType:

    return PaintingType(
        code=code,
        name=name,
        description=f"{name} painting",
        configuration=configuration,
        is_active=True
    )


class FakeDescriptionAnalyzer:

    def analyze(self, description):

        return (
            SubjectSpec(
                primary_subject="A woman",
                secondary_subjects=["river", "trees"],
                subject_relationships=[
                    "woman standing beside river"
                ]
            ),
            EnvironmentSpec(
                setting="peaceful riverside village",
                background_elements=[
                    "trees",
                    "small village houses"
                ],
                depth_elements=[
                    "river in foreground",
                    "trees in background"
                ]
            ),
            LightingSpec(
                lighting_condition="warm evening light",
                light_direction="light coming from the left",
                light_quality="soft golden light"
            ),
            ColorDirectionSpec(
                palette=[
                    "warm orange",
                    "gold",
                    "deep green",
                    "blue"
                ],
                contrast="moderate contrast",
                saturation="natural saturation"
            )
        )


def create_test_orchestrator():

    orchestrator = Orchestrator()

    orchestrator.description_analyzer = (
        FakeDescriptionAnalyzer()
    )

    return orchestrator


def test_prompt_contains_structured_description_information():

    painting_type = make_painting_type(
        code="oil",
        name="Oil",
        configuration={
            "visual_characteristics": [
                "rich painterly appearance"
            ],
            "color_tendencies": [
                "rich saturated pigments"
            ],
            "texture_characteristics": [
                "visible oil paint texture"
            ],
            "line_characteristics": [
                "soft painterly edges"
            ],
            "brush_characteristics": [
                "visible directional brushstrokes"
            ],
            "composition_tendencies": [
                "strong focal subject"
            ],
            "negative_constraints": [
                "avoid flat digital illustration"
            ]
        }
    )

    orchestrator = create_test_orchestrator()

    generation_spec = orchestrator.create_generation_spec(
        description="A woman standing beside a river",
        painting_type=painting_type,
        dimensions=DimensionRequest(
            width=1024,
            height=1024,
            unit="px"
        )
    )

    prompt = PromptCompiler().compile(
        generation_spec
    )

    assert "A woman" in prompt
    assert "river" in prompt
    assert "peaceful riverside village" in prompt
    assert "trees" in prompt
    assert "warm evening light" in prompt
    assert "soft golden light" in prompt
    assert "warm orange" in prompt
    assert "moderate contrast" in prompt


def test_prompt_contains_style_information():

    painting_type = make_painting_type(
        code="madhubani",
        name="Madhubani",
        configuration={
            "visual_characteristics": [
                "flat stylized forms"
            ],
            "color_tendencies": [
                "vivid traditional colors"
            ],
            "texture_characteristics": [
                "dense decorative patterning"
            ],
            "line_characteristics": [
                "bold dark outlines"
            ],
            "brush_characteristics": [
                "fine controlled strokes"
            ],
            "composition_tendencies": [
                "dense decorative framing"
            ],
            "negative_constraints": [
                "avoid photorealism"
            ]
        }
    )

    orchestrator = create_test_orchestrator()

    generation_spec = orchestrator.create_generation_spec(
        description="A woman standing beside a river",
        painting_type=painting_type,
        dimensions=DimensionRequest(
            width=1024,
            height=1024,
            unit="px"
        )
    )

    prompt = PromptCompiler().compile(
        generation_spec
    )

    assert "flat stylized forms" in prompt
    assert "vivid traditional colors" in prompt
    assert "dense decorative patterning" in prompt
    assert "bold dark outlines" in prompt
    assert "fine controlled strokes" in prompt
    assert "dense decorative framing" in prompt
    assert "avoid photorealism" in prompt


def test_prompt_contains_dimension_information():

    painting_type = make_painting_type(
        code="oil",
        name="Oil",
        configuration={}
    )

    orchestrator = create_test_orchestrator()

    generation_spec = orchestrator.create_generation_spec(
        description="A mountain landscape",
        painting_type=painting_type,
        dimensions=DimensionRequest(
            width=1600,
            height=900,
            unit="px"
        )
    )

    prompt = PromptCompiler().compile(
        generation_spec
    )

    assert "Width: 1600.0" in prompt
    assert "Height: 900.0" in prompt
    assert "Orientation: landscape" in prompt
    assert "Aspect ratio: 1.7778" in prompt


def test_different_painting_types_produce_different_prompts():

    configurations = {
        "oil": {
            "visual_characteristics": [
                "rich painterly appearance"
            ],
            "color_tendencies": [
                "rich saturated pigments"
            ],
            "texture_characteristics": [
                "visible oil paint texture"
            ],
            "line_characteristics": [
                "soft painterly edges"
            ],
            "brush_characteristics": [
                "visible directional brushstrokes"
            ],
            "composition_tendencies": [
                "strong focal subject"
            ],
            "negative_constraints": [
                "avoid flat digital illustration"
            ]
        },

        "watercolor": {
            "visual_characteristics": [
                "transparent painterly washes"
            ],
            "color_tendencies": [
                "transparent pigments"
            ],
            "texture_characteristics": [
                "visible watercolor paper grain"
            ],
            "line_characteristics": [
                "delicate lines"
            ],
            "brush_characteristics": [
                "fluid brush movement"
            ],
            "composition_tendencies": [
                "generous negative space"
            ],
            "negative_constraints": [
                "avoid thick opaque paint"
            ]
        },

        "acrylic": {
            "visual_characteristics": [
                "bold painted forms"
            ],
            "color_tendencies": [
                "strong saturated colors"
            ],
            "texture_characteristics": [
                "visible acrylic paint texture"
            ],
            "line_characteristics": [
                "confident edges"
            ],
            "brush_characteristics": [
                "confident brushstrokes"
            ],
            "composition_tendencies": [
                "clear focal hierarchy"
            ],
            "negative_constraints": [
                "avoid photorealistic CGI"
            ]
        },

        "madhubani": {
            "visual_characteristics": [
                "flat stylized forms"
            ],
            "color_tendencies": [
                "vivid traditional colors"
            ],
            "texture_characteristics": [
                "dense decorative patterning"
            ],
            "line_characteristics": [
                "bold dark outlines"
            ],
            "brush_characteristics": [
                "fine controlled strokes"
            ],
            "composition_tendencies": [
                "dense decorative framing"
            ],
            "negative_constraints": [
                "avoid photorealism"
            ]
        }
    }

    prompts = []

    orchestrator = create_test_orchestrator()

    compiler = PromptCompiler()

    for code, configuration in configurations.items():

        painting_type = make_painting_type(
            code=code,
            name=code.title(),
            configuration=configuration
        )

        generation_spec = (
            orchestrator.create_generation_spec(
                description="A woman standing beside a river",
                painting_type=painting_type,
                dimensions=DimensionRequest(
                    width=1024,
                    height=1024,
                    unit="px"
                )
            )
        )

        prompts.append(
            compiler.compile(
                generation_spec
            )
        )

    assert len(set(prompts)) == 4