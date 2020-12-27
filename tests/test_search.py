import pytest
from kaz.search import search

def test_search_string_returns_exact_match():
    items = { 'foo': 'bar' }
    assert search(items, 'foo') == items

def test_search_nonexistant_string_returns_empty_dictionary():
    items = { 'foo': 'bar' }
    assert search(items, 'baz') == {}

def test_search_string_with_question_mark_matches_any_character():
    items = {
        'bar': 'foo',
        'baz': 'foo'
    }
    assert search(items, 'ba?') == items

def test_search_asterisk_matches_any_string():
    items = {
        'foo': 'baz',
        'bar': 'baz'
    }
    assert search(items, '*') == items
