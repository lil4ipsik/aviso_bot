import json
from os import path as p

filelocation = p.dirname(p.abspath(__file__))

with open(filelocation + '/res/version.json') as f:
    data = json.load(f)

info = data['version']
nuitka = data['nuitka_version']

def version(n=False):
    if n:
        return nuitka
    return info