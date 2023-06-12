alf = 'ХОЧУНАБЮДЖЕТ'
a = set('ХЧНБДЖТ')
k = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf:
                        for i7 in alf:
                            for i8 in alf:
                                for i9 in alf:
                                    for i10 in alf:
                                        for i11 in alf:
                                            for i12 in alf:
                                                word = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11 + i12
                                                if len(set(word)) == len(a) and (set(word[1:8]) == a or set(word[2:9]) == a or set(word[3:10]) == a or set(word[4:11]) == a or set(word[5::]) == a):
                                                    k += 1
print(k)