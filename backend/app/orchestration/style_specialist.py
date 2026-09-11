from app.models.painting_type import PaintingType
from app.orchestration.generation_spec import StyleSpec


class StyleSpecialist:

    def create_style_spec(
        self,
        painting_type: PaintingType
    ) -> StyleSpec:

        configuration = painting_type.configuration

        return StyleSpec(
            painting_type=painting_type.name,
            visual_characteristics=configuration.get(
                "visual_characteristics",
                []
            ),
            color_tendencies=configuration.get(
                "color_tendencies",
                []
            ),
            texture_characteristics=configuration.get(
                "texture_characteristics",
                []
            ),
            line_characteristics=configuration.get(
                "line_characteristics",
                []
            ),
            negative_constraints=configuration.get(
                "negative_constraints",
                []
            )
        )