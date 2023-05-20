a = 'ЯРОСЛАВ'
gl = 'ЯОА'
sogl = 'РСЛВ'
b = set()
for i in range(len(a)):
    b.add(a[i])
k1 = 0
k2 = 0
k = 0
for i1 in b:
    for i2 in b:
        for i3 in b:
            for i4 in b:
                for i5 in b:
                    k1 = 0
                    k2 = 0
                    word = i1 + i2 + i3 + i4 + i5
                    if len(word) == len(set(word)):
                        for i in range(len(word)):
                            if word[i] in sogl:
                                k1 += 1
                            if word[i] in gl:
                                k2 += 1
                        word = word.replace('Я', '1')
                        word = word.replace('О', '1')
                        word = word.replace('А', '1')
                        word = word.replace('Р', '0')
                        word = word.replace('С', '0')
                        word = word.replace('Л', '0')
                        word = word.replace('В', '0')
                        if k1 > k2:
                            if '11' not in word:
                                k += 1
print(k)