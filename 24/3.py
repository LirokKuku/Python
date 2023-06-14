f = open('File/kompege.ru_files_zytAPLWaj.txt')
s = f.readline().split('D')

kmax = 0
for x in s:
    k = x.find('A')
    if k != -1:
        if k + 2 > kmax:
            kmax = k + 2
print(kmax)

