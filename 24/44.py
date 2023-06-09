f = open('File/244.txt')
r = f.readline()

r = r.replace('K', '')

maxx = 0
a = ''
b = []
for i in range(len(r) - 1):
    if r[i] + r[i + 1] == 'EM' or r[i] + r[i + 1] == 'ME':
        a += r[i] + r[i + 1]
    if r[i] + r[i + 1] == 'EE' or r[i] + r[i + 1] == 'MM':
        b.append(a)
        a = ''
print(len(max(b)))