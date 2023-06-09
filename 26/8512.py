f = open('File/26.txt')
s = []
# 210 2
# 987 5
for i in f:
    s.append(list(map(int, (i.split()))))
s.sort()

s = [-1] * 2
a = []
b = []
for x in range(len(s)):
