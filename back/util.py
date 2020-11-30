from random import choice
from string import ascii_letters, digits

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def randstr(lenght:int=32):
    return "".join(choice(ascii_letters+digits) for in range(lenght))