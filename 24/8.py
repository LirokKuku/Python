f = open('File/24_8.txt')
s = f.readline()

kmax = 0
alf = 'QWERTYUIOPASDFGHKLZCVBNM0987654321'
for b in alf:
    ss = s.split(b)
    for i in range(1, len(ss) -1):
        if len(ss[i]) + 2 > kmax:
            kmax = len(ss[i]) + 2
print(kmax)