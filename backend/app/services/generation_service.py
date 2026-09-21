from pathlib import Path

from sqlalchemy.orm import Session

from app.models.generation import Generation
from app.models.painting_type import PaintingType
from app.orchestration.orchestrator import Orchestrator
from app.orchestration.prompt_compiler import PromptCompiler
from app.providers.base import ImageGenerationProvider
from app.repositories.generation_repository import GenerationRepository
from app.schemas.dimension import DimensionRequest
from app.storage.image_storage import ImageStorage


class GenerationService:

    def __init__(
        self,
        provider: ImageGenerationProvider,
        storage: ImageStorage
    ):
        self.orchestrator = Orchestrator()
        self.prompt_compiler = PromptCompiler()

        self.provider = provider
        self.storage = storage

        self.repository = GenerationRepository()

    def generate(
        self,
        db: Session,
        description: str,
        painting_type: PaintingType,
        dimensions: DimensionRequest
    ) -> Generation:

        # ----------------------------------------
        # 1. Build the structured generation spec
        # ----------------------------------------

        generation_spec = (
            self.orchestrator.create_generation_spec(
                description=description,
                painting_type=painting_type,
                dimensions=dimensions
            )
        )

        # ----------------------------------------
        # 2. Compile the final AI prompt
        # ----------------------------------------

        prompt = self.prompt_compiler.compile(
            generation_spec
        )

        # ----------------------------------------
        # 3. Create database record
        # ----------------------------------------

        generation = Generation(
            description=description,
            painting_type=painting_type.code,

            width=generation_spec.dimensions.width,
            height=generation_spec.dimensions.height,
            unit=generation_spec.dimensions.unit,

            aspect_ratio=(
                generation_spec.dimensions.aspect_ratio
            ),

            orientation=(
                generation_spec.dimensions.orientation
            ),

            prompt=prompt,

            status="processing"
        )

        self.repository.create(
            db,
            generation
        )

        db.commit()
        db.refresh(generation)

        # ----------------------------------------
        # 4. Generate image
        # ----------------------------------------

        try:

            result = self.provider.generate(
                prompt=prompt,
                width=int(dimensions.width),
                height=int(dimensions.height)
            )

            # ------------------------------------
            # 5. Save image
            # ------------------------------------

            image_path = self.storage.save_image(
                result.image
            )

            # ------------------------------------
            # 6. Extract provider metadata
            # ------------------------------------

            model = None

            if result.metadata:
                model = result.metadata.get(
                    "model"
                )

            # ------------------------------------
            # 7. Update database record
            # ------------------------------------

            generation.provider = (
                result.provider_name
            )

            generation.model = model

            # Store a URL path instead of the
            # backend's local filesystem path.
            generation.image_path = (
                f"/generated/{Path(image_path).name}"
            )

            generation.status = "completed"

            generation.error_message = None

            self.repository.update(
                db,
                generation
            )

            db.commit()
            db.refresh(generation)

            return generation

        except Exception as exc:

            # ------------------------------------
            # Generation failed
            # ------------------------------------

            generation.status = "failed"

            generation.error_message = str(
                exc
            )

            self.repository.update(
                db,
                generation
            )

            db.commit()

            raise