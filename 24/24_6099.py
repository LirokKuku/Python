f = open('File/24-249.txt')
s = f.readline()
#
minn = 10**10
# for j in range(len(s)):
#     b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#     k = 0
#     for i in range(j, len(s)):
#         if s[i] in b:
#             b.remove(s[i])
#             k += 1
#         if s[i] not in b and len(b) != 0:
#             k += 1
#         if len(b) == 0:
#             minn = min(minn, k)
#     # if len(b) == 0:
#     #     break
# print(minn)
l = 0
l1 = 0
p = 16
p1 = 0
f = 0
e = 0
# s = '0123456789ABCDEFF'
b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
while e == 0:
    for i in b:
        if i in s[l:p:]:
            f = 0
        else:
            f = 1
            break
    if f == 0:
        if p - l < minn:
            minn = p - l
            l1 = l
            p1 = p
        l += 1
    else:
        if p + 1 <= len(s):
            p += 1
        else:
            e = 1
print(minn)
print(s[l1:p1:])