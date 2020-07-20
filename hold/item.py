from os import mkdir, remove
from os.path import join, exists
import json

from hold.constants import hold_home

def load():
    if not exists(hold_home):
        return {}
    with open(join(hold_home, 'items.json'), 'r') as f:
        items = json.load(f)
        for name, value in items.items():
            if value is None:
                # null value means it's a pointer to a binary file, load from blobs/{name}
                with open(join(hold_home, 'blobs', name), 'rb') as blob:
                    items[name] = blob.read()
        return items

def save(items, original_items):
    if not exists(hold_home):
        mkdir(hold_home)

    with open(join(hold_home, 'items.json'), 'w') as f:
        # write new item list
        for name, value in items.items():
            if type(value) is bytes:
                blobs = join(hold_home, 'blobs')
                if not exists(blobs):
                    mkdir(blobs)
                with open(join(blobs, name), 'w+b') as blob:
                    blob.write(value)
                items[name] = None
        # check for deleted items
        for name, value in original_items.items():
            if not name in items:
                # it was deleted, now delete the blob if the item was binary
                if type(value) is bytes:
                    remove(join(hold_home, 'blobs', name))

        json.dump(items, f)
