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
        group: str = 'dest_district'
    else:
        date: str = 'arrive_date '
        time: str = 'arrive_time'
        group: str = 'starting_district'

    return await prisma.horras.group_by(by=[group], where={
        'AND': [
            {
                date: {
                    'gte': date_lower,
                    'lte': date_upper
                }
            }, 
            {
                time: {
                    'gte': clock_lower,
                    'lte': clock_upper
                }
            }
        ]
    }, count=True)