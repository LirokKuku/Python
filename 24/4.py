f = open('File/kompege.ru_files_Yv4sIxmbs.txt')
s = f.readline()

k = 0
kmax = 0
for i in range(0, len(s) - 1, 2):
    if s[i] in 'CDF' and s[i + 1] in 'AO':
        k += 1
        kmax = max(kmax, k)
    else:
        k = 0
print(kmax)