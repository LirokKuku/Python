#https://inf-ege.sdamgia.ru/test?id=12887419&nt=True&pub=False
print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f = ((x == (not y)) <= (y and (not z))) or (z and (not w))
                if f == 0:
                    print(x, y, z, w)