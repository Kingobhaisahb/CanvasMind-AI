from dataclasses import dataclass
from typing import Any


@dataclass
class ImageGenerationResult:
    image_url: str | None = None
    image_bytes: bytes | None = None
    provider_name: str = "unknown"
    metadata: dict[str, Any] | None = None