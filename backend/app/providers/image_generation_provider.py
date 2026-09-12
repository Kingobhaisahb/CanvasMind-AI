from huggingface_hub import InferenceClient

from app.core.config import settings
from app.providers.base import ImageGenerationProvider
from app.providers.result import ImageGenerationResult


class HuggingFaceImageGenerationProvider(ImageGenerationProvider):

    def __init__(self):
        self.client = InferenceClient(
            api_key=settings.hf_token
        )

    def generate(
        self,
        prompt: str,
        width: int,
        height: int
    ) -> ImageGenerationResult:

        image = self.client.text_to_image(
            prompt=prompt,
            model=settings.hf_image_model
        )

        image_path = "generated_image.png"
        image.save(image_path)

        return ImageGenerationResult(
            provider_name="huggingface",
            metadata={
                "model": settings.hf_image_model,
                "width": width,
                "height": height,
                "image_path": image_path
            }
        )