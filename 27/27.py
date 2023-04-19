# https://kompege.ru/variant?kim=25023734 № 27A
n=1000
k=25
f = open('File/27B_7603.txt')
s = []
maxx = -1
for i in f:
    s.append(int(i))
for i1 in range(len(s) - 3):
    for i2 in range(i1 + 3, len(s)):
        maxx = max(maxx, s[i1] + s[i2])
print(maxx)