from horras_backend.database import prisma

async def find_records_in_range(date_lower: int, date_upper: int, clock_lower: int, clock_upper: int):
    records = await prisma.horras.find_many(
        where={
            "AND": [
                {
                    "departure_date": {
                        "gte": date_lower,
                    },
                    "arrive_date": {
                        "lt": date_upper,
                    },
                    "departure_time": {
                        "lte": clock_upper,
                    },
                    "arrive_time": {
                        "gte": clock_lower,
                    },
                }
            ]
        }
    )
    return records

async def find_num_records_in_range(date_lower: int, date_upper: int, clock_lower: int, clock_upper: int):
    num_records = await prisma.horras.count(
        where={
            "AND": [
                {
                    "departure_date": {
                        "gte": date_lower,
                    },
                    "arrive_date": {
                        "lt": date_upper,
                    },
                    "departure_time": {
                        "lte": clock_upper,
                    },
                    "arrive_time": {
                        "gte": clock_lower
                    },
                }
            ]
        }
    )
    return num_records