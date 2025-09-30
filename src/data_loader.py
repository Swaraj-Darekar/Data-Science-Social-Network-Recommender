import json

def load_data(filename):
    """
    Load JSON data from the given filename.
    
    """
    with open(filename, "r") as f:
        data = json.load(f)
    return data
