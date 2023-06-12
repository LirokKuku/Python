print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f = ((x <= y) or ((not w) == z)) and (x <= y) == (w and (not z))
                if f == 1:
                    print(x,y,z,w)
