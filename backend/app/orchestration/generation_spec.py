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
    negative_constraints: list[str]


class CompositionSpec(BaseModel):
    subject_placement: str
    framing: str
    negative_space: str
    balance: str


class GenerationSpec(BaseModel):
    description: str
    style: StyleSpec
    dimensions: DimensionSpec
    composition: CompositionSpec