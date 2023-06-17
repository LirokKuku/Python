from functools import lru_cache

def moves(h):
    a = h
    return (a + 1), (a + 5), (a * 3), (a * 6),

@lru_cache(None)
def f(h):
    if h >= 100:
        return 'I1'
    if 62 <= h < 100:
        return 'W'
    if any(f(x) == 'W' for x in moves(h)):
        return 'I1'
    if all(f(x) == 'I1' for x in moves(h)):
        return 'L1'
    if any(f(x) == 'L1' for x in moves(h)):
        return 'I2'
    if all(f(x) == 'I2' or f(x) == 'I1' for x in moves(h)):
        return 'L2'

for s in range(1, 62):
    ww = f((s))
    if ww == 'L2':
        print(s)