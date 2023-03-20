f = open('File/24_1.txt')
s = f.readlines().split('.')[1:-1]
mn = 10**10
for i in range(len(s)-5):
    ln = s[i] + s[i + 2] + s[i + 3] + s[i + 4] + s[i + 5]
    mn = min(mn, len(ln))
print(mn + 7)