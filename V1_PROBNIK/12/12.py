for n in range(1,100):

    #само условие
    s='>' + '0'*15 + '1'*n + '2'*18
    while (('>1' in s) or ('>2' in s) or ('>0' in s)):
        if (">1" in s):
            s=s.replace('>1', "22>", 1)
        if (">2" in s):
            s=s.replace('>2', "2>", 1)
        if (">0" in s):
            s=s.replace('>0', "1>", 1)
    s = s.replace('>', '')

    # проверка на простоту числа
    sum  = 0
    for i in range(0,len(s)):
        sum = sum + int(s[i])
    simple = True;
    for i in range(2, sum):
        if (sum%i)==0:
            simple=False;
            break
    if(simple==True):
        print(n, sum)