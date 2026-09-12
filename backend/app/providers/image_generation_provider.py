from typing import Any

from app.providers.base import ImageGenerationProvider


class DefaultImageGenerationProvider(ImageGenerationProvider):

    def generate(
        self,
        prompt: str,
        width: int,
        height: int
    ) -> Any:

        raise NotImplementedError(
            "Image generation provider is not configured yet."
        )