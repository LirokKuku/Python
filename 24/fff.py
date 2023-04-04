s = '012345'
b = ['0', '1', '3']
k = 0
for i in range(len(s)):
    if s[i] in b:
        b.remove(s[i])
print(s, b)