# print('x y z w')
# for x in (0, 1):
#     for y in (0, 1):
#         for z in (0, 1):
#             for w in (0, 1):
#                 f = ((not x) <= y) and ((not y) == z) and w
#                 if f == 1:
#                     print(x,y,z,w)

# k = 0
# for i in range(1000, 10000):
#     s = str(i)
#     if int(s[0]) % 4 == 0:
#         s = '9' + s[1::]
#     if int(s[0]) % 2 == 0 and int(s[0]) % 4 != 0:
#         s = '3' + s[1::]
#         print(s)
#     if s[0] == '9' and (oct(int(s))[-1]) == '4':
#         k += 1
# print(k)

# alf = 'POLYGN'
# k = 0
# for i1 in alf:
#     for i2 in alf:
#         for i3 in alf:
#             for i4 in alf:
#                 for i5 in alf:
#                     word = i1 + i2 + i3 + i4 + i5
#                     if word[0:3:] == word[2::] and (word[2] == 'O' or word[2] == 'Y'):
#                         k += 1
# print(k)

# for a in range(100, 0, -1):
#     k = 0
#     for x in range(1, 1000):
#         if (x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0)):
#             k += 1
#     if k == 999:
#         print(a)
#         break