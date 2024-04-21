import json

with open('res/version.json') as f:
    data = json.load(f)

info = data['version']

def version():
    return info