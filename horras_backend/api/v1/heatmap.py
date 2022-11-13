from fastapi import APIRouter
import horras_backend.model.heatmap.range_query as range_query

router = APIRouter()

MAX_DATE = 304
MAX_CLOCK = 1440

@router.get("/")
async def headmap():
    headmap_values = [[0 for i in range(MAX_CLOCK // 60)] for j in range(MAX_DATE)]
    for date in range(1, MAX_DATE):
        for time in range(0, MAX_CLOCK, 60):
            headmap_values
