from typing import List
import json 
from ..distrobution import SET_DISTRIBUTION

def find_categories():
    pass 

def parse_files(files:List[str]) -> List[str]:
    result = []
    for file in files: 
        f = open(file)
        data = json.load(f)
        f.close()
        for key, value in data["distribution"].items():
            if SET_DISTRIBUTION.lower() != key.lower():
                del data["distribution"][key]
        result.append(data)
    return result
    
