f = open('File/26_3.txt')
N = int(f.readline())
s = list(map(int, f.readlines()))
s.sort(reverse=True)

kmax = 0
while len(s) > 0:
    k = 0
    neisp = []
    isp = [s[0]]
    for box in s[1:]:
        if box <= isp[-1] - 11:
            isp.append(box)
        else:
            neisp.append(box)
    if len(isp) > kmax:
        kmax = len(isp)
        little_box = isp[-1]
    s = neisp.copy()
print(kmax, little_box)