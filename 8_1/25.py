for i in range(1017, 10**10, 1017):
    s = str(i)
    if s[0]=='2' and s[-1] == '1' and '7' in s and (s[2:6:] == '5432' or s[1:5:] == '5432'):
        print(i, i // 9601)