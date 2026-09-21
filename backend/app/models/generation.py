from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Generation(Base):
    __tablename__ = "generations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    painting_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True
    )

    width: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    height: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    unit: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    aspect_ratio: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    orientation: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    prompt: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    provider: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    model: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True
    )

    image_path: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="pending",
        index=True
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )