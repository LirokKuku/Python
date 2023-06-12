alf = 'АВОРТ'
k = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                k += 1
                word = i1 + i2 + i3 + i4
                if word == 'ВАТА':
                    print(k)