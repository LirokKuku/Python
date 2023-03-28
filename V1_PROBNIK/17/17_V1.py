f = open('File/17_1.txt')

sp = []
for i in f:
    sp.append(int(i))
maxx = 0
for i in sp:
    if i % 10 == 3:
        if i > maxx:
            maxx = i
maxx = maxx ** 2
maxs = 0
count = 0
for i in range(0, len(sp) -1):
    if (sp[i] % 10 == 3 and sp[i+1] % 10 != 3) or (sp[i] % 10 != 3 and sp[i+1] % 10 == 3):
        if sp[i]**2 + sp[i+1]**2 >= maxx:
            count += 1
            if sp[i]**2 + sp[i + 1] ** 2 > maxs:
                maxs = sp[i]**2 + sp[i+1]**2
print(count, maxs)