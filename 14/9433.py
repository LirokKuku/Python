a = 2**8 * 2**4 * 17333263511920313 * 4 + 2 ** 8

s = 0
while a > 0:
    if a % 111 == 1:
        s += 1
    a //= 111
print(s)