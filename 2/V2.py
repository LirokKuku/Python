print('x y w z f')
for x in (0, 1):
    for y in (0, 1):
        for w in (0 ,1):
            for z in (0, 1):
                f = ((y <= x) == (w <= (not z))) and (w or x)
                if f == 1:
                    print(x, y, w, z, f)