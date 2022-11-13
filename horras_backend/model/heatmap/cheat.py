import json
import os
from typing import List
from horras_backend.config import src_folder

def get_headmap() -> List[List[int]]:
    path = os.path.join(src_folder, "model", "heatmap", "heatmap.json")
    with open(path) as json_file:
        data = json.load(json_file)

    return data