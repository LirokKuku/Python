alf = 'ПРОЛИВ'
k = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf:
                        word = i1 + i2 + i3 + i4 + i5 + i6
                        if 'П' in word:
                            k += 1
print(k)