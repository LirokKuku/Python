f = open('File/24_6.txt')
s = f.readline().split('D')

kmax = 0
for i in range(len(s) - 2):
    if len(s[i] + s[i+1] + s[i + 2]) + 2 > kmax:
        kmax = len(s[i] + s[i + 1] + s[i + 2]) + 2
print(kmax)