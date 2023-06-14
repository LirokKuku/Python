f = open('File/24_7.txt')
s = f.readline()

k = 1 #!!!
kmax = 0
for i in range(len(s) - 1):
    if not(s[i] in 'NOP' and s[i + 1] in 'NOP'):
        k += 1
        kmax = max(kmax, k)
    else:
        k = 1
print(kmax)