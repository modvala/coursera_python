import argparse
import os
import tempfile
import json

def add(key, value, data):
    if key not in data.keys():
        data[key] = value
    else:
        data[key] = data[key]+', '+value
    #print(data)
    return data

def get(key, data):
    #print(key, data.keys())
    if key not in data.keys():
       return None
    else:
       return data[key]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--value")
    arg = parser.parse_args()
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    tempfile.TemporaryFile(storage_path)
    with open(storage_path, 'r+') as f:
            storage = f.read()
            data = dict(json.loads(json.loads(json.JSONEncoder().encode(storage))))    
    if arg.value is None:
        print(get(arg.key, data))
    else:
        data = add(arg.key,arg.value, data)
        with open(storage_path, 'w+') as f:
            json.dump(data, f)
