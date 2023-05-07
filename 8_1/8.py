alf = '012345678'
k = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf:
                        word =  i1 + i2 + i3 + i4 + i5 + i6
                        if (word[0] == word[1]) or (word[2] == word[1]) or (word[2] == word[3]) or (word[3] == word[4]) or (word[4] == word[5]):
                            k += 1
print(k)