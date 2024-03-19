from .lexer import lex as _lex
from .parser import parse as _parse

def parse(json):
    tokens = _lex(json)
    data, tokens = _parse(tokens)
    if len(tokens) != 0:
        raise Exception("Error: didn't consume all tokens")
    return data
