from fastapi import APIRouter
from horras_backend.api.v1.heatmap import router as heatmap_router
from horras_backend.api.v1.geometry import router as geometry_router


router = APIRouter()
router.include_router(heatmap_router, prefix="/heatmap", tags=["heatmap"])
router.include_router(geometry_router, prefix="/geometry", tags=["geometry"])