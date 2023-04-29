f = open('File/24.txt')
s = f.readline()

s = s.replace('C', 'A')
a = 'AB'
while a in s:
    a += 'AB'
print((len(a) - 2)//2)