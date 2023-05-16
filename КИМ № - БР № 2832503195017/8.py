alf = ['А', 'П', 'Е', 'Л', 'Ь', 'С', 'И', 'Н']
sogl = 'ПЛСН'
k = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf:
                        for i7 in alf:
                            word = i1 + i2 + i3 + i4 + i5 + i6 + i7
                            if len(set(word)) == len(word) and (word[word.index('Ь') - 1] in sogl and word[word.index('Ь') + 1] in sogl) and 'Ь' in word[1:6:]:
                                k += 1
print(k)