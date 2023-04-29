f = open('Files/17_A.txt')
s = [int(x) for x in f.readlines()]

mins = 10**10
c = 0
minn = min(s)
for i in range(len(s) -1):
    if (s[i] % 11 + s[i + 1] % 11) == minn:
        c += 1
        mins = min(mins, s[i] + s[i + 1])
print(c, mins)