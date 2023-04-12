# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6095
f = open('File/26-104.txt')
s = []
for i in f:
    s.append(list(map(int, (i.split()))))
s.sort()
maxr = 0
maxl = 0
while len(s) != 0:
    line = 0
    count = 1
    r = s[0][0]
    sp = []
    sp.append(s[0][1])
    s[0] = 0
    for i in range(1, len(s)):
        if s[i][0] == r:
            sp.append(s[i][1])
            s[i] = 0
        else:
            break
    sp = list(set(sp))
    sp.sort()
    for i in range(len(sp) - 1):
        if sp[i] + 1 == sp[i + 1]:
            count += 1
        else:
            if count >= 5:
                line += 1
            count = 1
    if line >= maxl:
        maxl = line
        maxr = r
    while 0 in s:
        s.remove(0)
print(maxl, maxr)
    # print(s[0][0])