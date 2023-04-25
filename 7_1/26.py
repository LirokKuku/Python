f = open('File/26.txt')
s = [int(x) for x in f.readlines()]
s.sort()
s = s[::-1]
sp = []
spm = []
minn = 10**10
while len(s) != 0:
    if len(sp) == 0:
        sp.append(s[0])
        minn = min(minn, s[0])
        s[0] = 0
    for i in range(1, len(s)):
        if s[i] + 7 <= min(sp):
            sp.append(s[i])
            s[i] = 0
    while 0 in s:
        s.remove(0)
    spm.append(sp)
    sp = []
print(minn, len(spm))