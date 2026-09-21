from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.v1.routes import router
from app.database.base import Base
from app.database.connection import engine

from app.models.generation import Generation
from app.models.painting_type import PaintingType
from app.models.user import User


app = FastAPI(
    title="AI Painting Studio",
    version="1.0.0"
)


# Create database tables
Base.metadata.create_all(
    bind=engine
)


# Include API routes
app.include_router(router)


# Directory containing generated images
generated_images_directory = Path(
    "app/storage/generated"
)

generated_images_directory.mkdir(
    parents=True,
    exist_ok=True
)


# Serve generated images
app.mount(
    "/generated",
    StaticFiles(
        directory=str(generated_images_directory)
    ),
    name="generated"
)


@app.get("/")
def root():
    return {
        "message": "AI Painting Studio API is running"
    }