alf = ['А', 'В', 'О', 'Р', 'Т']
alf = sorted(alf)
print(alf)
k = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf:
                        k += 1
                        word = i1 + i2 + i3 + i4 + i5 + i6
                        if word == 'ВОРОТА':
                            print(k)