f = open('File/26_9474.txt')
n = f.readline()
k = f.readline()

for i in f:
    s = list(map(int, i.readline().split()))
print(s)