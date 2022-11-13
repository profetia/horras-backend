from typing import List
from fastapi import APIRouter
# import horras_backend.model.heatmap.range_query as range_query
import horras_backend.model.heatmap.cheat_sheet as cheat_sheet

router = APIRouter()

MAX_DATE = 304
MAX_CLOCK = 1440

@router.get("/")
async def headmap() -> List[List[int]]:
    # headmap_values = [[0 for i in range(MAX_CLOCK // 60)] for j in range(MAX_DATE)]
    # for date in range(1, MAX_DATE):
    #     for time in range(0, MAX_CLOCK, 60):
    #         headmap_values[date][time // 60] = await range_query.find_num_records_in_range(date, date + 1, time, time + 60)
    headmap_values = cheat_sheet.get_headmap_values()
    return headmap_values
