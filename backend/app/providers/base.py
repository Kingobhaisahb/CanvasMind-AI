from abc import ABC, abstractmethod
from typing import Any


class ImageGenerationProvider(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str,
        width: int,
        height: int
    ) -> Any:
        """
        Generate an image from a prompt and dimensions.

        Every image-generation provider must implement
        this method.
        """
        pass