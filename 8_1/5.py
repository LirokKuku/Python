k = 0
for i in range(1, 1000):
    s = bin(i)[2::]
    if i % 2 == 0:
        s = '1' + s + '00'
    else:
        s = s + bin(s.count('1'))[2::]
    s = int(s, 2)
    if s < 190:
        print(i)
        k += 1
print(k)