from os import mkdir
from os.path import join, expanduser, exists
import json

hold_home = expanduser(join('~', '.hold'))

def load():
    if not exists(hold_home):
        return {}
    with open(join(hold_home, 'items.json'), 'r') as f:
        return json.load(f)

def save(items):
    if not exists(hold_home):
        mkdir(hold_home)
    with open(join(hold_home, 'items.json'), 'w') as f:
        json.dump(items, f)
