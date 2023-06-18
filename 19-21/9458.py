# from functools import lru_cache
#
# def moves(h):
#     a, b = h
#     return ((2*a)**2, b**2), (a**2, (b + 3)**2), (a**2, (b+4)**2)
#
# @lru_cache(None)
# def f(h):
#     if sum(h) >= 196:
#         return 'W'
#     if any(f(x) == 'W' for x in moves(h)):
#         return 'P1'
#     if all(f(x) == 'P1' for x in moves(h)):
#         return 'V1'
#     if any(f(x) == 'V1' for x in moves(h)):
#         return 'P2'
#     if all(f(x) == 'P2' for x in moves(h)):
#         return 'V2'
#
# for s in range(1, 14):
#     ww = f((3, s))
#     print(ww, s)
def game(s1, s2, h):
    if (h == 5) and (s1*s1 + s2*s2 >= 196):
        return 1
    if (h == 5) and (s1*s1 + s2*s2 < 196):
        return 0
    if (h < 5) and (s1*s1 + s2*s2 >= 196):
        return 0
    else:
        if h % 2 == 0:
            return game(s1 * 2, s2, h + 1) or game(s1, s2 + 3, h + 1) or game(s1, s2 + 4, h + 1)
        else:
            return game(s1 * 2, s2, h + 1) and game(s1, s2 + 3, h + 1) and game(s1, s2 + 4, h + 1)


for i in range(1, 14):
    if game(3, i, 1) == 1:
        print(i)