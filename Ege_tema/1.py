f = open('27-A_3231.txt')
s = list(map(int, f.readlines()[1:]))

mn = []

for i in range(len(s)):
    summ = 0
    for j in range(len(s)):
        summ += min(((j - i) % len(s)), (i - j) % len(s)) * s[j]
    mn.append(summ)
for i in range(len(mn)):
    if mn[i] == min(mn):
        print(i+1)
print(mn)

         