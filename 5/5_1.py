alf = '012'
def f(x, k):
    s = ''
    while x > 0:
        s = alf[x % k] + s
        x //= k
    return s
for n in range(1, 1001):
    r = f(n, 3)
    if n % 5 == 0:
        r = r + r[-3::]
    else:
        r = r + f((n % 5) * 5, 3)
    r = int(r, 3)
    if r < 5496:
        print(n)