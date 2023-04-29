a = 6 * 512**195 + 7 * 64**196 + 3 * 8**193 + 200

s = 0
l = set()
while a > 0:
    if a % 64 == 0:
        s += 1
    l.add(a % 64)
    a //= 64
print(s, l)