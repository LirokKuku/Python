# 100 1000 2000
f = open('File/26-124.txt')
s = [int(x) for x in f.readlines()]
s.sort(reverse=True)

r = [1000] * 100
k = 0
for j in range(len(s)):
    for i in range(len(r)):
        if s[j] <= r[i]:
            r[i] = r[i] - s[j]
            k += 1
            break
print(k, sum(r))