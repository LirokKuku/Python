#№14
min = 10**10
for x in range(0, 13):
    for y in range(0, 13):
        a = 7 * 13 ** 4 + 7 * 13 ** 3 + x * 13 ** 2 + 2 * 13 + y
        b = 3 * 17 ** 4 + y * 17 ** 3 + 3 * 17 ** 2 + 4 * 17 + x
        c = a + b
        if (c % 61 == 0) and (c < min):
            min = c
print(min//61)