f = open('FIle/24.txt')
s = f.readline().split('O')
k = 0
for i in range(len(s)):
    if s[i].count('E') == 2:
        k += 1
print(k)