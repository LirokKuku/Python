f = open('File/kompege.ru_files_QA4XnU4ZP.txt')
s = f.readline()

k = 0
kmax = 0
for i in range(len(s)):
    if s[i] in 'ABC':
        k += 1
        if k > kmax:
            kmax = k # kmax = max(k, kmax)
    else:
        k = 0
print(kmax)