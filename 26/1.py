f = open('File/26_1.txt')
N = int(f.readline())
s = list(map(int, f.readlines()))
# s = [int(x) for x in f.readlines()]
summ = 0
a = [] # цена больше ста
for x in s:
    if x <= 100:
        summ += x
    else:
        a.append(x)
a.sort()
for i in range(len(a)):
    if i < len(a) // 2:
        summ += a[i] * 0.7
        maxprtice= a[i]
    else:
        summ += a[i]
print(summ, maxprtice)