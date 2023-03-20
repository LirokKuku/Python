f = open('24_2.txt')
s = f.readlines()
alf = 'XYZWOP'
mx= 0
for i in alf:
    mx = max(mx, s.count('X' + i + 'P'))
print(mx)