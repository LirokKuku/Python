from functools import lru_cache

def moves(h):
    a, b = h
    return (a + 2, b), (a * 3, b), (a, b + 2), (a, b * 3)

@lru_cache(None)
def f(h):
    if sum(h) >= 183:
        return 'W'
    if any(f(x)=='W' for x in moves(h)):
        return 'P1'
    if all(f(x)=='P1' for x in moves(h)):
        return 'V1'
    if any(f(x)=='V1' for x in moves(h)):
        return 'P2'
    if all(f(x)=='P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'
    return None

for s in range(1, 165):
    ww = f((18,s))
    if ww =='V2':
        print(s, ww)