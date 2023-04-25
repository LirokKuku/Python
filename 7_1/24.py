f = open('File/24.txt')
s = f.readline()
s = s.replace('C', 'A')
b = []
k = 0
a = ''
for i in range(0, len(s), 2):
    if 'AB' == s[i] + s[i + 1]:
        a += 'AB'
    else:
        b.append(a)
        a = ''
print(len(max(b)))