from app.models.painting_type import PaintingType
from app.orchestration.orchestrator import Orchestrator
from app.orchestration.prompt_compiler import PromptCompiler
from app.providers.base import ImageGenerationProvider
from app.providers.result import ImageGenerationResult
from app.schemas.dimension import DimensionRequest


class GenerationService:

    def __init__(
        self,
        provider: ImageGenerationProvider
    ):
        self.orchestrator = Orchestrator()
        self.prompt_compiler = PromptCompiler()
        self.provider = provider

    def generate(
        self,
        description: str,
        painting_type: PaintingType,
        dimensions: DimensionRequest
    ) -> ImageGenerationResult:

        generation_spec = self.orchestrator.create_generation_spec(
            description=description,
            painting_type=painting_type,
            dimensions=dimensions
        )

        prompt = self.prompt_compiler.compile(
            generation_spec
        )

        result = self.provider.generate(
            prompt=prompt,
            width=int(dimensions.width),
            height=int(dimensions.height)
        )

        return result