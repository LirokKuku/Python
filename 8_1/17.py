f = open('FIle/17.txt')
s = [int(x) for x in f.readlines()]

b = []
for i in range(len(s) - 1):
    a = []
    if (s[i] % 10 == 6 and s[i+1] % 10 != 6) or (s[i] % 10 != 6 and s[i+1] % 10 == 6):
        a.append(s[i])
        a.append(s[i + 1])
        b.append(a)
print(len(b), sum(max(b)))