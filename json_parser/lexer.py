def lex_string(string):
    json_string = ""
    if string[0] != '"':
        raise Exception("should start with opening double quote")

    for c in string[1:]:
        if c == '"':
            break

        json_string += c

    return json_string

def lex_number(string):
    length = 0
    for c in string:
        if not c.isnumeric():
            break
        length += 1

    return int(string[:length]), length


def lex(string):
    tokens = []

    idx = 0;
    while idx < len(string):
        c = string[idx]
        if c in ['{', '}', ":", '[', ']']:
            tokens.append(c)
            idx += 1

        elif c == '"':
            json_string = lex_string(string[idx:])
            tokens.append(json_string)
            idx += len(json_string) + 2
        elif c.isnumeric():
            num, length = lex_number(string[idx:])
            tokens.append(num)
            idx += length
        elif string[idx:idx+4] == "null":
            tokens.append(None)
            idx += 4
        elif string[idx:idx+4] == "true":
            tokens.append(True)
            idx += 4
        elif string[idx:idx+5] == "false":
            tokens.append(False)
            idx += 5
        else:
            idx += 1

    return tokens
