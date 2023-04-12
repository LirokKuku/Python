f = open('FIle/26_7602.txt')
s = []
count = 0
for i in f:
    s.append(list(map(int, i.split())))
s.sort()
sp = [0] * 210
for i in range(len(s)):
    for j in range(len(sp)):
        if s[i][0] > sp[j]:
            sp[j] = s[i][1]
            count += 1
            num = j
            break
print(num+1)
print(count)