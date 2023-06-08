print('a b c')
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            f = (a == (b or b)) <= c
            if f == 1:
                print(a, b, c)