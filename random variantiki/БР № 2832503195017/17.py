f = open('File/17_5292.txt')
s = [int(x) for x in f.readlines()]

minn = 10**10
for i in range(len(s)):
    if s[i] % 123 == 0:
        minn = min(minn, s[i])

b = []
for i in range(len(s) - 1):
    a = []
    if (s[i] % 2023 < minn and s[i+1] % 2023 >= minn) or (s[i] % 2023 >= minn and s[i+1] % 2023 < minn):
        a.append(s[i])
        a.append(s[i+1])
        b.append(a)
print(len(b), sum(max(b)))