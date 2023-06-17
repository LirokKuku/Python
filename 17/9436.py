f = open('Files/17_9436.txt')
s = [int(x) for x in f.readlines()]

alf = '012345'
def f(x, k):
    s = ''
    while x > 0:
        s = alf[x % k] + s
        x //= k
    return s

a = []
b = []
for i in range(len(s) - 1):
    if str(f((abs(s[i] + s[i - 1])), 5))[-2::] == '14' and str(s[i]).count('3') == 2:
        a.append(s[i])
        a.append(s[i+1])
        b.append(a)
        a = []
print(len(b), sum(max(b)))