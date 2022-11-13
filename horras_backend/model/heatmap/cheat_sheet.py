import json
import os
from typing import List
from horras_backend.config import src_folder

def get_headmap_values() -> List[List[int]]:
    heatmap_value_path = os.path.join(src_folder, "model", "heatmap", "heatmap_data.json")
    with open(heatmap_value_path) as json_file:
        headmap_values = json.load(json_file)

    return headmap_values