import json
from os.path import join

import pytest

from kaz.item import load, save

@pytest.fixture(autouse=True)
def setup_kaz_home(tmp_path, monkeypatch):
    # Set kaz home directory to a temporary directory
    # All operations will take place in this temporary directory
    monkeypatch.setattr('kaz.item.kaz_home', tmp_path)

def test_save_with_new_item_writes_new_item(tmp_path):
    # Add foo: bar
    original_items = {}
    items = { 'foo': 'bar' }

    save(items, original_items)

    with open(tmp_path / 'items.json', 'r') as f:
        written = json.load(f)
    assert written == items

def test_save_with_new_blob_writes_blob_to_file(tmp_path):
    original_items = {}
    items = { 'foo': b'Hello' }

    save(items, original_items)

    with open(tmp_path / 'blobs' / 'foo', 'rb') as f:
        blob = f.read()
    assert blob == b'Hello'

def test_save_remove_blob_removes_file(tmp_path):
    # Add blob (which creates the file for the blob)
    test_items = { 'foo': b'' }
    save(items=test_items, original_items={})

    save(items={}, original_items=test_items)

    blob_path = tmp_path / 'blobs'
    blobs = list(blob_path.iterdir())
    assert len(blobs) == 1 and blobs[0].name == 'foo'

def test_load_with_no_items_returns_empty_dictionary(tmp_path):
    with open(tmp_path / 'items.json', 'w') as f:
        json.dump({}, f)

    assert load() == {}

def test_load_with_one_item_returns_dictionary_with_one_item(tmp_path):
    with open(tmp_path / 'items.json', 'w') as f:
        json.dump({ 'foo': 'bar' }, f)

    assert load() == { 'foo': 'bar' }

def test_load_with_one_blob_returns_dictionary_with_blob_contents(tmp_path):
    contents = b'Hello'
    with open(tmp_path / 'items.json', 'w') as f:
        json.dump({ 'foo': None }, f)
    blob_path = tmp_path / 'blobs'
    blob_path.mkdir()
    with open(blob_path / 'foo', 'wb') as f:
        f.write(contents)

    assert load() == { 'foo': contents }
