f = open('File/24_9441.txt')
s = f.readline()
s = s.replace('B', 'C')
s = s.split('A')
print(max(s))