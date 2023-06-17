s = '3' * 21 + '4' * 22 + '5' * 23
while '333' in s or '4444' in s or '55555' in s:
    if '333' in s:
        s = s.replace('333', '44')
    else:
        if '4444' in s:
            s = s.replace('4444', '555')
        else:
            if '55555' in s:
                s = s.replace('55555', '3')
k = 0
for i in range(len(s)):
    k += int(s[i])
print(k,s)