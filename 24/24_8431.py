f = open('File/24_8431.txt')
s = f.readline()
# s = 'BADZXYZKLMENYZXXX'
sp = ['XYZ', 'XZY', 'YZX', 'YXZ', 'ZYX', 'ZXY']
flag = 0
k = 0
maxln = 0
for i in range(len(s) - 2):
    if flag > 0:
        flag -= 1
    else:
        s1 = s[i:i+3:]
        if s1 in sp:
            maxln=max(maxln, k)
            if s[i + 1:i + 4:] not in sp:
                flag = 2
            k = 0
        else:
            k += 1
print(maxln)