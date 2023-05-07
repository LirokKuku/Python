from functools import lru_cache

def moves(h):
    a = h
    if a * 2 <= 60:
        return (a + 1), (a + 2), (a * 2)
    if a + 2 <= 60:
        return (a + 1), (a + 2)
    return ((a + 1)),

@lru_cache(None)
def f(h):
    if h >= 51:
        return 'W'
    if any(f(x) == 'W' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' and f(x) != 'P1' for x in moves(h)):
        return 'V2'

for s in range(1, 51):
    ww = f((s))
    if ww == 'V2':
        print(s, ww)