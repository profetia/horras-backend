from fastapi import APIRouter
from .heatmap import router as headmap_router

router = APIRouter()
router.include_router(headmap_router, prefix="/heatmap", tags=["heatmap"])