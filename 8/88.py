alf = '0123456'
ch = set('0246')
nech = set('135')
k = 0
k1 = 0
k2 = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf:
                        word = i1 + i2 + i3 + i4 + i5 + i6
                        if word[-1] != '0' and word[-1] != '1' and word[-1] != '2' and word[-1] != '3':
                            k1 = 0
                            k2 = 0
                            for i in range(len(word)):
                                if word[i] in ch:
                                    k1 += 1
                                else:
                                    k2 += 1
                                if k1 == 3 and k2 == 3:
                                    k += 1
print(k)