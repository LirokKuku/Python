f = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210 - 255

s=''
while f > 0:
    s = s + str(f % 8)
    f //= 8
print(s.count('0'))