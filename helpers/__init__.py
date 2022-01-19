import json

def to_json(data):
    data = json.dumps(data, indent=2, sort_keys=True, default=str)
    return data.encode()
