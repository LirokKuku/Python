f = open('File/17.txt')
s = list(map(int, f.readlines()))
mn = 10**10
for i in s:
    if str(i)[-1] == '5':
        mn = min(i, mn)
a = []
for i in range(len(s) - 1):
    if (s[i] + s[i + 1]) % mn == 0:
        if (len(str(s[i])) == 3 and len(str(s[i + 1])) != 3) or (len(str(s[i + 1])) == 3 and len(str(s[i])) != 3):
            a.append(s[i] ** 2 + s[i + 1]**2)
print(len(a), max(a))