def f(x, y):
    a = bin(x)[2::]
    b = bin(y)[2::]
    while len(a) > len(b):
        b = '0' + b
    while len(b) > len(a):
        a = '0' + a
    for i in range(len(a)):
        if int(a[i]) > int(b[i]):
            b = a[i] +b[1::]
    return int(b, 2)

for a in range(1, 1001):
    t = True
    for x in range(1, 1001):
        k = (((f(x, 42) > 64)) and (f(x, 34)<= 102)) <= (not(f(x, a) < 70))
        if k == 0:
            t = False
            break
    if t:
        print(a)