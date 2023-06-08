alf = 'АБОЛТ'
alf1 = 'АО'
alf2 = 'БЛТ'
k = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf2:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf1:
                        k += 1
                        word = i1 + i2 + i3 + i4 + i5 + i6
                        if 'БОЛОТО' == word:
                            print(k)
                            break