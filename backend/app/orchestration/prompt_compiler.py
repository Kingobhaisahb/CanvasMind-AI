from app.orchestration.generation_spec import GenerationSpec


class PromptCompiler:

    def compile(
        self,
        generation_spec: GenerationSpec
    ) -> str:

        style = generation_spec.style
        dimensions = generation_spec.dimensions
        composition = generation_spec.composition

        visual_characteristics = ", ".join(
            style.visual_characteristics
        )

        color_tendencies = ", ".join(
            style.color_tendencies
        )

        texture_characteristics = ", ".join(
            style.texture_characteristics
        )

        line_characteristics = ", ".join(
            style.line_characteristics
        )

        negative_constraints = ", ".join(
            style.negative_constraints
        )

        prompt = f"""
Create a {style.painting_type} painting depicting:

{generation_spec.description}

ARTISTIC CHARACTERISTICS:
{visual_characteristics}

COLOR DIRECTION:
{color_tendencies}

TEXTURE:
{texture_characteristics}

LINE AND MARK-MAKING:
{line_characteristics}

COMPOSITION:
{composition.subject_placement}
{composition.framing}
{composition.negative_space}
{composition.balance}

CANVAS:
{dimensions.width} x {dimensions.height} {dimensions.unit}
{dimensions.orientation} orientation
Aspect ratio: {dimensions.aspect_ratio}

AVOID:
{negative_constraints}
"""

        return prompt.strip()