from os import mkdir
from os.path import join, expanduser, exists
import json

stash_home = expanduser(join('~', '.stash'))

def load():
    if not exists(stash_home):
        return {}
    with open(join(stash_home, 'items.json'), 'r') as f:
        return json.load(f)

def save(items):
    if not exists(stash_home):
        mkdir(stash_home)
    with open(join(stash_home, 'items.json'), 'w') as f:
        json.dump(items, f)
