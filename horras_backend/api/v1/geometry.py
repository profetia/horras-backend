from typing import Dict, List
from fastapi import APIRouter
import horras_backend.model.geometry.queries as queries
from horras_backend.model.heatmap.ranges import TimeRange

router = APIRouter()

def convert_to_dict(data: List[Dict], field: str) -> Dict:
    return {item[field]: item['_count']['_all'] for item in data}

@router.get("/")
async def geometry(query: TimeRange):
    date_lower, date_upper = query.date_range
    clock_lower, clock_upper = query.clock_range
    
    departure_records: List[Dict] = await queries.find_records_group(
        date_lower, date_upper, clock_lower, clock_upper, "departure"
    )
    departure_dict: Dict[int, int] = convert_to_dict(departure_records, 'starting_district')
    
    arrive_records: List[Dict] = await queries.find_records_group(
        date_lower, date_upper, clock_lower, clock_upper, "arrive"
    )
    arrive_dict: Dict[int, int] = convert_to_dict(arrive_records, 'dest_district')

    final_dict: Dict[int, Dict] = {}
    for key in set(departure_dict.keys()).union(set(arrive_dict.keys())):
        final_dict[key] = {
            'start_num': departure_dict.get(key, 0),
            'dest_num': arrive_dict.get(key, 0)
        }

    records: List[Dict[str, int]] = [{'id': key, **value} for key, value in final_dict.items()]

    return records