import json

m functools import wraps
def to_json(func):
    @wraps(func)
    def to_j(*args, **kwargs):
        return  json.loads(*args, **kwargs)
    return to_j
