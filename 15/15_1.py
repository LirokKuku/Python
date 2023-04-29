from itertools import product
print('p q a f')
for p, q, a in product([0, 1], repeat = 3):
    print(p, q, a, int(p <= ((q and (not a)) <= (not p))))