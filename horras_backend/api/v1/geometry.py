from typing import Dict, List, Tuple
from fastapi import APIRouter
import horras_backend.model.geometry.queries as queries
from horras_backend.model.heatmap.ranges import TimeRange

router = APIRouter()

def convert_to_dict(data: List[Dict], field: str) -> Dict[Tuple[int, int], Dict[str, int]]:
    return {(item[f"{field}_lat_group"], item[f"{field}_lng_group"]): {
        "id": item[f"{field}_district"], 
        "count": item["_count"]["_all"]
    } for item in data}

@router.get("/")
async def geometry(query: TimeRange):
    date_lower, date_upper = query.date_range
    clock_lower, clock_upper = query.clock_range
    
    departure_records: List[Dict] = await queries.find_records_group(
        date_lower, date_upper, clock_lower, clock_upper, "departure"
    )

    departure_dict: Dict[Tuple[int, int], Dict[str, int]] = convert_to_dict(departure_records, 'starting')
    
    arrive_records: List[Dict] = await queries.find_records_group(
        date_lower, date_upper, clock_lower, clock_upper, "arrive"
    )
    arrive_dict: Dict[Tuple[int, int], Dict[str, int]] = convert_to_dict(arrive_records, 'dest')

    final_dict: Dict[Tuple[int, int], Dict[str, int]] = {}
    for key in set(departure_dict.keys()).union(set(arrive_dict.keys())):
        final_dict[key] = {
            'id': arrive_dict[key]['id'] if key in arrive_dict else departure_dict[key]['id'],
            'start_num': departure_dict[key]['count'] if key in departure_dict else 0,
            'dest_num': arrive_dict[key]['count'] if key in arrive_dict else 0,
        }

    records: List[Dict[str, int]] = [
        {
            'lat': key[0], 
            'lng': key[1], 
            **value, 
        } for key, value in final_dict.items()
    ]

    return records