print('a b c d')
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            for d in (0, 1):
                f = ((a and b) == (not c)) and (b <= d)
                if f == 1:
                    print(a,b,c,d, f)