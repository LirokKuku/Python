f = open('10.txt')
N = int(f.readline())
t = [0] * (10**6 + 1)
for s in f:
    enter, leave = map(int, s.split())
    t[enter] += 1
    t[leave] -= 1
k = 0 # количество людей на данный момент
cnt = 0 # количество моментов, когда в автобусе кто-то был,
# то когда k != 0
maxk = 0
for i in t:
    k += i
    maxk = max(maxk, k)
    if k != 0:
        cnt += 1
print(maxk, cnt)
    
    
    
    
    