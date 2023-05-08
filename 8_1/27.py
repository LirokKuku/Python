f = open('FIle/27.txt')
s = [int(x) for x in f.readlines()]

b = []
for i in range(len(s)):
    a = []
    a.append(i+1)
    a.append(s[i])
    b.append(a)

x = []
p = []
for i in range(len(s) - 3):
    for j in range(3):
        if s[i]