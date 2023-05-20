# 888. 900 85 33(6406)
f = open('File/26-119.txt')
a = [0]*85
b = [0]*33

s = []
for i in f:
    s.append(list(map(int, i.split())))
s.sort()


l = 0
m = 0
n = 0
for i in s:
    if i[2] == 1:
        flag = 0
        for j in range(len(a)):
            if i[0] >= a[j]:
                a[j] = (i[0] + i[1])
                flag = 1
                l += 1
                break
        if flag == 0:
            for j in range(len(b)):
                if i[0] >= b[j]:
                    b[j] = (i[0] + i[1])
                    flag = 1
                    l += 1
                    break
        if flag == 0:
            n += 1
    else:
        flag = 0
        for j in range(len(b)):
            if i[0] >= b[j]:
                b[j] = (i[0] + i[1])
                flag = 1
                m += 1
                break
        if flag == 0:
            n += 1
print(n, m)