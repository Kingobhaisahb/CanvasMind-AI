from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class PaintingTypeResponse(BaseModel):
    id: int
    code: str
    name: str
    description: str
    configuration: dict[str, Any]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)