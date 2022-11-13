from typing import List
from fastapi import APIRouter
# import horras_backend.model.heatmap.queries as queries
import horras_backend.model.heatmap.cheat as cheat

router = APIRouter()

@router.get("/")
async def headmap() -> List[List[int]]:
    # clock_range = queries.CLOCK_UPPER_BOUND - queries.CLOCK_LOWER_BOUND
    # date_range = queries.DATE_UPPER_BOUND - queries.DATE_LOWER_BOUND
    # headmap_values = [[0 for i in range(clock_range // 60)] for j in range(date_range)]
    # for date in range(1, date_range):
    #     for clock in range(0, clock_range, 60):
    #         headmap_values[date][clock // 60] = await queries.find_records_count(date, date + 1, clock, clock + 60)
    data = cheat.get_headmap()
    return data
