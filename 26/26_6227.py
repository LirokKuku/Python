# 300 100
f = open('File/26-108.txt')
sd = []
s = []
for i in f:
    sp = list(map(int, i.split()))
    if len(sp) == 4:
        ball=sp[1]+sp[2]+sp[3]
    else:
        ball = sp[1]+sp[2]+max(sp[3], sp[4])
    if sp[0] == 1:
        s.append(ball)
        sd.append(ball)
    else:
        s.append(ball)
sd.sort(reverse=True)
s.sort(reverse=True)
print(s[99], sd[99])
for i in range(len(sd)):
    print(i, sd[i])
for i in range(len(s)):
    print(i, s[i])