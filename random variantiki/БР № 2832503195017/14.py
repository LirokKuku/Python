f = 4**625 - 2**311 + 2**571 - 48

s=''
while f > 0:
    s = s + str(f%4)
    f //= 4
print(s.count('1'))