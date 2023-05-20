# 52455 1236147000
# 6 1000
b = 1000
f = open('FIle/26_1.txt')
s = []
for i in f:
    s.append(list(map(int, i.split())))
s.sort()
k = 0
for i in range(len(s)):
    if s[i][1] == 0 and s[i][0] >= b:
        s[i][1] = 10**10
    if (s[i][0] == 0 and s[i][1] < b) or (s[i][0] < 0 and s[i][-1] < b):
        s[i] = []
    if sum(s[i]) == 0:
        k += 1
        s[i] = []
while [] in s:
    s.remove([])

