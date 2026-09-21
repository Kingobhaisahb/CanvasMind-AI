from dataclasses import dataclass
from typing import Any

from PIL import Image


@dataclass
class ImageGenerationResult:
    image: Image.Image
    provider_name: str
    metadata: dict[str, Any] | None = None