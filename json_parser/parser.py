def parse_array(tokens):
    tok = tokens[0]
    if tok == ']':
        return [], tokens[1:]

    vals = []
    while True:
        val, tokens = parse(tokens)
        vals.append(val)

        tok = tokens[0]
        if tok == ']':
            return vals, tokens[1:]

def parse_object(tokens):
    tok = tokens[0]
    if tok == '}':
        return {}, tokens[1:]

    obj = {}
    while True:
        if tok == '}':
            return obj, tokens[1:]

        obj[tok] =  tokens[2]

        if len(tokens) >= 4 and tokens[3] == ',':
            tokens = tokens[4:]
        else:
            tokens = tokens[3:]

        tok = tokens[0]


def parse(tokens):
    if tokens[0] == '[':
        return parse_array(tokens[1:])
    if tokens[0] == '{':
        return parse_object(tokens[1:])

    return tokens[0], tokens[1:]

        
