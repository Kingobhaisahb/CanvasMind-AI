from pydantic import BaseModel, Field


class DimensionSpec(BaseModel):
    width: float = Field(gt=0)
    height: float = Field(gt=0)
    unit: str
    aspect_ratio: float
    orientation: str


class StyleSpec(BaseModel):
    painting_type: str

    visual_characteristics: list[str]

    color_tendencies: list[str]

    texture_characteristics: list[str]

    line_characteristics: list[str]

    brush_characteristics: list[str]

    composition_tendencies: list[str]

    negative_constraints: list[str]


class SubjectSpec(BaseModel):
    primary_subject: str

    secondary_subjects: list[str] = Field(
        default_factory=list
    )

    subject_relationships: list[str] = Field(
        default_factory=list
    )


class EnvironmentSpec(BaseModel):
    setting: str

    background_elements: list[str] = Field(
        default_factory=list
    )

    depth_elements: list[str] = Field(
        default_factory=list
    )


class LightingSpec(BaseModel):
    lighting_condition: str

    light_direction: str

    light_quality: str


class ColorDirectionSpec(BaseModel):
    palette: list[str] = Field(
        default_factory=list
    )

    contrast: str

    saturation: str


class CompositionSpec(BaseModel):
    subject_placement: str

    framing: str

    negative_space: str

    balance: str


class GenerationSpec(BaseModel):
    description: str

    subject: SubjectSpec

    environment: EnvironmentSpec

    style: StyleSpec

    composition: CompositionSpec

    dimensions: DimensionSpec

    lighting: LightingSpec

    color_direction: ColorDirectionSpec