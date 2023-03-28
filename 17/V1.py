f = open('Files/17_1.txt', 'r')

sp = []
minn = 10000
count = 0

for i in f:
    sp.append(str(int(i)))
    if (sp[-1][-1::] == '1') and (int(sp[-1]) < minn):
        minn = int(sp[-1])

minn = minn**2

for i in range(0, len(sp) -1):
    if sp[i][-1::] == sp[i+1][-1::]:
        if ((int(sp[i]) % 3 == 0) and (int(sp[i+1]) % 3 != 0)) or ((int(sp[i]) % 3 != 0) and ((int(sp[i+1])) % 3 == 0)):
            if (int(sp[i]) ** 2 +int(sp[i+1])**2)< minn:
                count += 1

print(count)