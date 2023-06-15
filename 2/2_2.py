print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f = ((not x) or y or (not z) or w) and (not((not x) or w))
                if f == 1:
                    print(x, y, z, w)