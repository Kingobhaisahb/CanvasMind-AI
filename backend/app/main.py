from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine
from app.models.painting_type import PaintingType


app = FastAPI(
    title="AI Painting Studio API",
    version="1.0.0",
    description="AI-powered painting generation SaaS"
)


Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Painting Studio API"
    }