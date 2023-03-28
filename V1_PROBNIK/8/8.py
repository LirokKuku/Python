alf = 'ВОДР'
k = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf:
                        for i7 in alf:
                            word = i1 + i2 + i3 + i4 + i5 + i6 + i7
                            if word.count('О') == 3 and word.count('Д')==2 and word.count('Р')==1 and word.count('В')==1 and 'ОО' not in word:
                                k += 1
print(k)