f = open('File/kompege.ru_files_sJDwcyfWx.txt')
s = f.readline()

k = 0
kmax = 0
for i in range(2, len(s) - 2, 3):
    if (s[i] == 'A' and s[i + 2] == 'A') or (s[i] == 'C' and s[i + 2] == 'C'):
        k += 1
        if k > kmax: kmax = k
    else:
        k = 0
print(kmax)