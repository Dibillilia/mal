import re
from copy import deepcopy

class Reader():
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokens.reverse()  # reverse the tokens so pop is performant

    def next(self):
        return self.tokens.pop()

    def peek(self):
        return self.tokens[-1]

    def __str__(self):
        rev = deepcopy(self.tokens)
        rev.reverse()
        return "Reader([" + ",".join(rev) + "])"


tokens = re.compile(r'[\s,]*(~@|[\[\]{}()\'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}(\'"`,;)]*)')


def tokenize(user_string):
    atoms = [a for a in tokens.findall(user_string) if a]
    return atoms


def read_list(token_reader):
    mal_list = []
    while token_reader.peek() != ")":
        mal_list.append(read_form(token_reader))
    return mal_list


def read_atom(token_reader):
    atom = token_reader.next()
    try:
        return int(atom)
    except ValueError:
        return atom


def read_form(token_reader):
    if token_reader.peek() == "(":
        token_reader.next()  # we don't need the (
        return read_list(token_reader)
    else:
        return read_atom(token_reader)


def read_str(user_string):
    token_reader = Reader(tokenize(user_string))
    return read_form(token_reader)
