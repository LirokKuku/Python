from itertools import product

f = open('File/27a_8491.txt')
a = int(f.readline())
b = int(f.readline())
c = f.readline()
s = [int(x) for x in f.readlines()]

s1 = s.copy()
s1.sort(reverse=True)

print(s1[0:21])
print(s.index(9993), s.index(9978), s.index(9978, 344), s.index(9977), s.index(9974), s.index(9964), s.index(9950), s.index(9949), s.index(9947), s.index(9913, 635), s.index(9904), s.index(9903), s.index(9898), s.index(9894), )
maxx = 0
for x1 in range(0, a - 7 * b):
    for x2 in range(x1 + b + 1, a - 6 * b):
        for x3 in range(x2 + b + 1, a - 5 * b):
            for x4 in range(x3 + b + 1, a - 4 * b):
                for x5 in range(x4 + b + 1, a - 3 * b):
                    for x6 in range(x5 + b + 1, a - 2 * b):
                        for x7 in range(x6 + b + 1, a - b):
                            for x8 in range(x7 + b + 1, a):
                                maxx = max(maxx, s[x1]+s[x2]+s[x3]+s[x4]+s[x5]+s[x6]+s[x7]+s[x8])
print(maxx)