from app.orchestration.generation_spec import GenerationSpec


class PromptCompiler:

    def compile(
        self,
        generation_spec: GenerationSpec
    ) -> str:

        subject = generation_spec.subject
        environment = generation_spec.environment
        lighting = generation_spec.lighting
        color_direction = generation_spec.color_direction
        style = generation_spec.style
        composition = generation_spec.composition
        dimensions = generation_spec.dimensions

        secondary_subjects = ", ".join(
            subject.secondary_subjects
        )

        subject_relationships = ", ".join(
            subject.subject_relationships
        )

        background_elements = ", ".join(
            environment.background_elements
        )

        depth_elements = ", ".join(
            environment.depth_elements
        )

        palette = ", ".join(
            color_direction.palette
        )

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

        brush_characteristics = ", ".join(
            style.brush_characteristics
        )

        composition_tendencies = ", ".join(
            style.composition_tendencies
        )

        negative_constraints = ", ".join(
            style.negative_constraints
        )

        prompt = f"""
Create a {style.painting_type} painting.

SUBJECT:
Primary subject: {subject.primary_subject}

Secondary subjects:
{secondary_subjects or "None specified"}

Subject relationships:
{subject_relationships or "None specified"}

ENVIRONMENT:
Setting: {environment.setting}

Background elements:
{background_elements or "None specified"}

Depth elements:
{depth_elements or "None specified"}

LIGHTING:
Condition: {lighting.lighting_condition}
Direction: {lighting.light_direction}
Quality: {lighting.light_quality}

COLOR DIRECTION:
Palette: {palette or "Not specifically specified"}
Contrast: {color_direction.contrast}
Saturation: {color_direction.saturation}

ARTISTIC CHARACTERISTICS:
{visual_characteristics}

STYLE COLOR TENDENCIES:
{color_tendencies}

TEXTURE:
{texture_characteristics}

LINE AND MARK-MAKING:
{line_characteristics}

BRUSH AND PAINT APPLICATION:
{brush_characteristics}

STYLE COMPOSITION TENDENCIES:
{composition_tendencies}

COMPOSITION:
Subject placement: {composition.subject_placement}
Framing: {composition.framing}
Negative space: {composition.negative_space}
Balance: {composition.balance}

CANVAS:
Width: {dimensions.width}
Height: {dimensions.height}
Unit: {dimensions.unit}
Orientation: {dimensions.orientation}
Aspect ratio: {dimensions.aspect_ratio}

ORIGINAL USER DESCRIPTION:
{generation_spec.description}

AVOID:
{negative_constraints}

Create a cohesive finished painting. Preserve the described subject,
environment, lighting, and color information while strongly applying
the specified painting type and its artistic characteristics.
""".strip()

        return prompt