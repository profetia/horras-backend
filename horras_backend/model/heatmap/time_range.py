from typing import Tuple
from pydantic import BaseModel

class TimeRange(BaseModel):
    date_range: Tuple[int, int]
    clock_range: Tuple[int, int]