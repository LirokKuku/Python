def dels(x):
    a = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            a.append(i)
            if x//i != i:
                a.append(x//i)
    return a

def pros(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

