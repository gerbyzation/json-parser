from .parser import parse

def test_parse_array():
    assert parse(['[', ']']) == ([], [])
    assert parse(['[', '[', ']', ']']) == ([[]], [])
    assert parse(['[', '[', ']', '[', ']', ']']) == ([[], []], [])
    assert parse(['[', '[', '[', ']', ']', ']']) == ([[[]]], [])

def test_parse_types():
    assert parse(['[', 'name', 1, None, True, False, ']']) == (['name', 1, None, True, False], [])


def test_parse_obj():
    assert parse(['{', '}']) == ({}, [])
    assert parse(['{', 'name', ':', 'package', '}']) == ({'name': 'package'}, [])
    assert parse(['{', 'name', ':', 'package', ',', 'version', ':', 'three', '}']) == ({'name': 'package', 'version': "three"}, [])

    assert parse(['{', 'name', ':', 'package', 'version', ':', 3 , 'private', ':', False, '}']) == ({'name': 'package', 'version': 3, 'private': False}, [])
