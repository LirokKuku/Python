print('x y z')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            f = (y <= x) and (x <= z)
            if f == 1:
                print(x, y, z)