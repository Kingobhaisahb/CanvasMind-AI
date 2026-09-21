from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.dimensions import router as dimensions_router
from app.api.v1.generations import router as generations_router
from app.api.v1.painting_types import router as painting_types_router


router = APIRouter(prefix="/api/v1")

router.include_router(auth_router)
router.include_router(dimensions_router)
router.include_router(painting_types_router)
router.include_router(generations_router)