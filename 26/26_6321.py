# 20 3500
f = open('File/26-112.txt')

bank_n = [0] * 20
bank_k = [0] * 20
bank_c = [0] * 20
s = []
for i in f:
    s.append(list(map(int, i.split())))
s.sort(key = lambda x: x[0])
# s.sort()
for i in range(len(s)):
    minn = min(bank_k)
    nomer = bank_k.index(minn)
    if s[i][0] <= bank_k[nomer]:
        bank_n[nomer] = bank_k[nomer]
        if bank_n[nomer] >= 1440:
            break
        bank_k[nomer] += s[i][1]
    if s[i][0] > bank_k[nomer]:
        bank_n[nomer] = s[i][0]
        if bank_n[nomer] >= 1440:
            break
        bank_k[nomer] = s[i][0]+s[i][1]
    bank_c[nomer] += 1
print(min(bank_c))
minn = min(bank_c)
nomer = bank_c.index(minn)
print(bank_n[nomer])