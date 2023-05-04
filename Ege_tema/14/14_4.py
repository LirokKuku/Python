for A in range(1,1000):
    fl = True
    for x in range(1, 1000):
        f = ((x%2==0) <= (x%13!=0)) or (x + A >= 1000)
        if f == 0: # if not f:            fl = False            break    if fl == True:
        print(A)
        break
