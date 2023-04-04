f = open('File/24-249.txt')
s = f.readline()

minn = 10**10
b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
k = 0
for i in range(len(s)):
    if s[i] in b:
        b.remove(s[i])
        k += 1
    if s[i] not in b and len(b) != 0:
        k += 1
    if len(b) == 0:
        minn = min(minn, k)
        k = 0
        b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    print(minn, b, k)
print(minn)