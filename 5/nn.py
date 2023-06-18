# for n in range(1, 1001):
# #     s = bin(n)[2::]
# #     if n % 3 == 0:
# #         s = s + s[-3::]
# #     else:
# #         s = s + bin((n % 3) * 3)[2::]
# #     r = int(s, 2)
# #     if r < 76:
# #         print(n)
# for n in range(1, 1001):
#     s = bin(n)[2::]
#     if s.count('1') % 3 == 0:
#         s = s + s[1:3]
#     else:
#         s = s + bin((s.count('1') % 3) * 3)[2::]
#     r = int(s, 2)
#     if r < 60:
#         print(n)
alf = '0123456'
# def f(x, k):
#     s = ''
#     while x > 0:
#         s = alf[x%k] + s
#         x //= k
#     return s
#
# k = 0
# for n in range(343, 2402):
#     s = f(n, 7)
#     if s[-1] in '02468':
#         s = '6' + s
#     else:
#         s = '5' + s
#     r = int(s, 7)
#     if r > 14500:
#         k += 1
# print(k)
for n in range(63, 1001):
    s = bin(n)[2::]
    if s.count('1') % 2 == 0:
        a = s[-4::]
        a = a.replace('1', '*')
        a = a.replace('0', '1')
        a = a.replace('*', '1')
        s = s[0:-4] + a
    else:
        b = s
        a = s[-4:-1]
        a = a.replace('1', '*')
        a = a.replace('0', '1')
        a = a.replace('*', '1')
        s = s[0:-4] + a + b[-1]
    if n > 63:
        print(int(s, 2) , n)
