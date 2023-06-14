f = open('File/kompege.ru_files_EHtApFlt0.txt')
s = f.readline()

k = 0
kmax = 0
for i in range(0, len(s) - 1, 2):
    if s[i] in 'ABC' and s[i + 1] in 'ABC':
        k += 1
        kmax = max(kmax, k)
    else:
        k = 0
print(kmax)