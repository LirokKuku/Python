# print('x y z w')
# for x in (0, 1):
#     for y in (0, 1):
#         for z in (0, 1):
#             for w in (0, 1):
#                 f = ((not w) and ((z or y) <= ((not x) and z)))
#                 if f == 1:
#                     print(x,y,z,w)
# #
# maxx = 0
# minn = 0
# k = 0
# for i in range(300, 700+1):
#     s = str(i)
#     if s[0] != '0' and s[1] != '0' and s[0] >= s[1] >= s[2]:
#         maxx = int(s[0] + s[1])
#         minn = int(s[1] + s[2])
#     if s[0] != '0' and s[1] != '0' and s[1] >= s[0] >= s[2]:
#         maxx = int(s[1] + s[0])
#         minn = int(s[0] + s[2])
#     if s[2] != '0' and s[1] != '0' and s[2] >= s[1] >= s[0]:
#         maxx = int(s[2] + s[1])
#         minn = int(s[1] + s[0])
#     if s[0] != '0' and s[2] != '0' and s[0] >= s[2] >= s[1]:
#         maxx = int(s[0] + s[2])
#         minn = int(s[2] + s[1])
#     if s[1] != '0' and s[2] != '0' and s[1] >= s[2] >= s[1]:
#         maxx = int(s[1] + s[2])
#         minn = int(s[2] + s[1])
#     if s[0] != '0' and s[2] != '0' and s[2] >= s[0] >= s[1]:
#         maxx = int(s[2] + s[0])
#         minn = int(s[0] + s[1])
#     if s[1] == s[2] and s[1] == '0':
#         maxx = int(s[0] + s[1])
#         minn = maxx
#     if s[1] == '0':
#         if int(s[0]) > int(s[2]):
#             maxx = int(s[0] + s[2])
#             minn = int(s[2] + s[1])
#     if s[2] == '0':
#         if int(s[0]) > int(s[1]):
#             maxx = int(s[0] + s[1])
#             minn = int(s[1] + s[2])
#     if (maxx - minn) == 43:
#         k +=1
# print(k)
#
# alf = 'КАРТИН'
# sogl = 'КРТН'
# gl = 'АИ'
# k = 0
# for i1 in alf:
#     for i2 in alf:
#         for i3 in alf:
#             for i4 in alf:
#                 for i5 in alf:
#                     word = i1 + i2 + i3 + i4 + i5
#                     if word[0] in gl and word[1] in sogl and word[2] in gl and word[3] in sogl and word[4] in gl:
#                         k +=1
#                     if word[0] in sogl and word[1] in gl and word[2] in sogl and word[3] in gl and word[4] in sogl:
#                         k += 1
# print(k)
#
# for n in range(1, 2000):
#     s = '>2' + '12' * n + '<'
#     print(s)
#     while '>2<' not in s:
#         s = s.replace('>1', '>2', 1)
#         s = s.replace('12<', '1<2', 1)
#         s = s.replace('>21', '1>', 1)
#         s = s.replace('1<', '<2', 1)
#         if '><' in s:
#             break
#         if s.count('1') + s.count('2') > 141:
#             print(n)
#             exit()
#
# F = [0]*(100 + 1)
# summ = ''
# summ1 = 0
# for n in range(100 + 1):
#     if n <3:
#         F[n]=1
#     if n > 2 and n % 2 == 0:
#         F[n] = F[n-2] + F[n-1] + 2*n
#     if n > 2 and n % 2 != 0:
#         F[n] = F[n-1]-F[n-2]-3*n
#     summ =str(F[100])
#     for i in range(len(summ)):
#         summ1 += int(summ[i])
# print(summ1)
# from functools import lru_cache
#
# def moves(h):
#     a = h
#     x, y = 1, 3
#     return (a + x), (a * y)
#
# @lru_cache(None)
# def f(h):
#     if h >= 65:
#         return 'W'
#     if any(f(x) == 'W' for x in moves(h)):
#         return 'P1'
#     if all(f(x) == 'P1' for x in moves(h)):
#         return 'V1'
#     if any(f(x) == 'V1' for x in moves(h)):
#         return 'P2'
#     if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
#         return 'V2'
#
# for s in range(1, 65):
#     ww = f((s))
#     if ww == 'P2':
#         print(s, ww)
# №14
# min = 10** 10
# for x in range(0, 13):
#     for y in range(0, 13):
#         a = 7 * 13 ** 4 + 7 * 13 ** 3 + x * 13 ** 2 + 2 * 13 + y
#         b = 3 * 17 ** 4 + y * 17 ** 3 + 3 * 17 ** 2 + 4 * 17 + x
#         c = a + b
#         if (c % 61 == 0) and (c < min):
#             min = c
# print(min//61)
#
f = open('Files/17_1.txt', 'r')

sp = []
minn = 10000
count = 0

for i in f:
    sp.append(str(int(i)))
    if (sp[-1][-1::] == '1') and (int(sp[-1]) < minn):
        minn = int(sp[-1])

minn = minn**2

for i in range(0, len(sp) -1):
    if sp[i][-1::] == sp[i+1][-1::]:
        if ((int(sp[i]) % 3 == 0) and (int(sp[i+1]) % 3 != 0)) or ((int(sp[i]) % 3 != 0) and ((int(sp[i+1])) % 3 == 0)):
            if (int(sp[i]) ** 2 +int(sp[i+1])**2)< minn:
                count += 1

print(count)