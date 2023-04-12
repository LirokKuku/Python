# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6092
f = open('File/26-101.txt')
s = [int(x) for x in f]
s = sorted(s, reverse=True)

sp = list()
spBig = []
c = 0
while c == 0:
    if len(sp) == 0:
        sp.append(s[0])
        s[0] = 0
    for i in range(1, len(s)):
        if s[i] + 9 <= min(sp):
            sp.append(s[i])
            s[i] = 0
    while 0 in s:
        s.remove(0)
    spBig.append(sp)
    sp = []
    if len(s)==0:
        c += 1
print(len(spBig), len(max(spBig)))