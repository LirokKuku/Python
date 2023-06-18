# print('x y z')
# for x in (0, 1):
#     for y in (0, 1):
#         for z in (0, 1):
#             f = (x == y) or ((y or z) <= x)
#             if f == 0:
#                 print(x,y,z)
# print('x y z w')
# for x in (0, 1):
#     for y in (0, 1):
#         for z in (0, 1):
#             for w in (0, 1):
#                 f = ((not z) == (not y)) or ((not x) and y) or w
#                 if f == 0:
#                     print(x,y,z,w)
#
print('x y z w f1 f2')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f1 = (w <= z) == (y <= x)
                f2 = (w <= z) and ((not x) == y)
                if f1 == 1 and f2 == 0:
                    print(x,y,z,w,f1,f2)