from fastapi import APIRouter

from app.api.v1.painting_types import router as painting_types_router


router = APIRouter(
    prefix="/api/v1"
)

router.include_router(
    painting_types_router
)