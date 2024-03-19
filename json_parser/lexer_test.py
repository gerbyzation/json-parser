from .lexer import lex, lex_string, lex_number

def test_lex_string():
    assert lex_string('"this is a string"') == "this is a string"
    assert lex_string('"json-parser"') == "json-parser"

def test_lex_number():
    assert lex_number("1 ") == (1, 1)
    assert lex_number("12") == (12, 2)
    assert lex_number("12 ") == (12, 2)

def test_lex():
    assert lex('{"name": "json-parser"}') == ['{', "name", ":", "json-parser", "}"]
    assert lex('{"private": true, "published": false}') == ['{', "private", ":", True, "published", ":", False, "}"]
    assert lex('["name", "json-parser"]') == ['[', "name", "json-parser", "]"]
    assert lex('["name", 1, null]') == ['[', "name", 1, None, ']']
