# clck.ru/R7tyJ
from functools import lru_cache

def moves(h):
    a, b = h
    if a * 2 <= 50: #ограничение по количеству камней
        return (a+1, 0), (a+2,0), (a*2,b) #пишем ходы
    if a + 2 <= 50:
        return (a+1, 0), (a+2,0)
    return (a+1, 0),

@lru_cache(None)
def f(h):
#    if sum(h)>80: #условие проигрыша
#         return "П1"
    if sum(h)>=41: #условие победы
        return 'W'
    elif any(f(x) == 'W' for x in moves(h)):
        return 'П1'
    elif all(f(x) == 'П1' for x in moves(h)):
        return 'В1'
    elif any(f(x) == 'В1' for x in moves(h)):
        return 'П2'
    elif all(f(x) == 'П1' or f(x) == 'П2' for x in moves(h)):
        return 'В2'
    elif any(f(x) == 'В2' for x in moves(h)):
        return 'П3'
    elif all(f(x) == 'П1' or f(x) == 'П2' or f(x) == 'П3' for x in moves(h)):
        return 'В3'
#     return None

for s in range(40,0,-1): #диапазон для s
    ww = f((s,0))
    if ww == 'В3': 
        print(s, ww) #количество камней в кучах

    
    
