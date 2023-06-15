alf = '0123456789AB'
ch = '02468B'
nch = '13579A'
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf:
                        for i7 in alf:
                            word = i1 + i2 + i3 + i4 + i5 + i6
                            if word.count('B') == 2 and