def f1(x,y,w,z):
    return int((x or (not y)) <= (w == z))
def f2(x, y, w, z):
    return int((x or (not y)) == (z <= w))
print('x y w z f1 f2')
from itertools import product
for x, y, w, z in product([0,1], repeat = 4):
    print(x, y, w, z, f1(x, y, w, z),'', f2(x, y, w, z))