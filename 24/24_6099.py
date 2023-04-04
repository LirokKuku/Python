f = open('File/24-249.txt', 'r')
s = f.readline()

minn = 10000000000000000
k = 0
b = ['0', '1', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
for i in range(len(s)):
    if s[i] in b:
        k += 1
        b.remove(str(s[i]))
    if len(b) != 0 and s[i] not in b:
        k += 1
    if len(b) == 0:
        minn = min(minn, k)
        b = ['0', '1', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        k = 0
print(minn)