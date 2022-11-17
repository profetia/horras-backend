from typing import Dict, List
from horras_backend.database import prisma

async def find_records_group(date_lower: int, 
                            date_upper: int, 
                            clock_lower: int, 
                            clock_upper: int, 
                            kind: str) -> List[Dict]:
    if kind == "departure":
        date: str = 'departure_date'
        time: str = 'departure_time'
        group: str = ['starting_district', 'starting_lng_group', 'starting_lat_group']
    else:
        date: str = 'arrive_date '
        time: str = 'arrive_time'
        group: str = ['dest_district', 'dest_lng_group', 'dest_lat_group']

    return await prisma.horras.group_by(by=group, where={
        'AND': [
            {
                date: {
                    'gte': date_lower,
                    'lt': date_upper
                }
            }, 
            {
                time: {
                    'gte': clock_lower,
                    'lt': clock_upper
                }
            }
        ]
    }, count=True)

