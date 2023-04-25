for A in range(1000):
    B = True
    for x in range(1000):
        if ((x&39==0) or ((x&11==0)<=(x&A!=0)))==0:
            B=False
    if B:
        print(A)
        break