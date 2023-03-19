k  =0
for i in range(1, 10000):
    s = bin(i)[2::]
    for j in range(2):
        s = s + str(s.count('1') % 2)
    s = int(s, 2)
    if 40 <= s <= 90:
        k += 1
print(k)