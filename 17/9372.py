f = open('Files/17_9372.txt')
s = [int(x) for x in f.readlines()]


maxx = -10**10
for i in range(len(s)):
    if abs(s[i]) % 1001 == 0:
        maxx = max(maxx, abs(s[i]))


a = []
b = []
for i in range(len(s) - 1):
    a = []
    if len((str(s[i]))) == 3 or len((str(s[i + 1]))) == 3:
        if s[i] + s[i+1] > abs(maxx):
            a.append(s[i])
            a.append(s[i + 1])
            b.append(a)
print(len(b), sum(min(b)))