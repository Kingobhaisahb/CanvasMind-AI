from abc import ABC, abstractmethod

from app.providers.result import ImageGenerationResult


class ImageGenerationProvider(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str,
        width: int,
        height: int
    ) -> ImageGenerationResult:
        """
        Generate an image from a prompt and dimensions.

        Every image-generation provider must implement
        this method.
        """
        pass