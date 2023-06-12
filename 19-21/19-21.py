from functools import lru_cache

def moves(h):
    a, b = h
    return (a + 2, b), (a * 2, b), (a, b + 2), (a, b * 2),

@lru_cache(None)
def f(h):
    if sum(h) >= 123:
        return 'W'
    elif any(f(x) == 'W' for x in moves(h)):
        return 'P1'
    elif all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    elif any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    elif all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'


for s in range(1, 41):
    ww = f((3, s))
    print(s, ww)