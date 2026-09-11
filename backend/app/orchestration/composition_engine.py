from app.orchestration.generation_spec import (
    CompositionSpec,
    DimensionSpec
)


class CompositionEngine:

    def create_composition_spec(
        self,
        description: str,
        dimensions: DimensionSpec
    ) -> CompositionSpec:

        if dimensions.orientation == "landscape":
            subject_placement = (
                "Place the primary subject slightly off-center "
                "to create a balanced horizontal composition."
            )

            framing = (
                "Use a wide framing that takes advantage "
                "of the horizontal canvas."
            )

            negative_space = (
                "Maintain moderate negative space around "
                "the primary subject."
            )

            balance = (
                "Balance the primary subject with supporting "
                "visual elements across the horizontal canvas."
            )

        elif dimensions.orientation == "portrait":
            subject_placement = (
                "Place the primary subject along the central "
                "vertical axis with controlled vertical spacing."
            )

            framing = (
                "Use vertical framing that emphasizes the "
                "height of the canvas."
            )

            negative_space = (
                "Maintain controlled negative space above "
                "and around the primary subject."
            )

            balance = (
                "Create vertical visual balance between the "
                "subject and supporting elements."
            )

        else:
            subject_placement = (
                "Place the primary subject near the center "
                "while maintaining visual balance."
            )

            framing = (
                "Use a centered framing suited to a square canvas."
            )

            negative_space = (
                "Maintain balanced negative space around "
                "the primary subject."
            )

            balance = (
                "Maintain radial or symmetrical visual balance."
            )

        return CompositionSpec(
            subject_placement=subject_placement,
            framing=framing,
            negative_space=negative_space,
            balance=balance
        )