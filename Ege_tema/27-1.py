def f(x):
    a = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            a.add(i)
            a.add(x // i)
    return sorted(list(a))
r = 25
d = f(9009)[::-1]
dels = {}
for i in d:
    dels[i] = [0] * 4 
buf = []
cnt = 0
ff = open('27_1b.txt')
N = int(ff.readline())
for _ in range(r):
    buf.append(int(ff.readline()))
for _ in range(r, N):
    x = int(ff.readline())
    for i in d:
        if buf[0] % i == 0:
            dels[i][buf[0] % 4] += 1
            break
    for i in d:
        if (x * i) % 9009 == 0:
            cnt += dels[i][(4 - x % 4) % 4]
    buf = buf[1:] + [x]
print(cnt)
    
    
