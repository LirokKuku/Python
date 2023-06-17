f = open('File/kpolyakov.spb.ru_cms_files_ege-stream_72_27-72b.txt')
N = int(f.readline())
a = list(map(int, f.readlines()))

cnt = 0
summ = [0] * 71
summ[0] = 1
s = 0
for x in a:
    s += x
    cnt += summ[s % 71]
    summ[s % 71] += 1
print(cnt)

# cnt = 0
# for i in range(len(s)):
#     summ = 0
#     for j in range(i, len(s)):
#         summ += s[j]
#         if summ % 71 == 0:
#             cnt += 1
# print(cnt)