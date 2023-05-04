for A in range(1, 1000):
    fl = True
    for x in range(1,1000):
        f = (x&13==0)<=((x&40!=0)<=(x&A!=0))
        if f == 0:  # if not f:                fl = False                break    if fl==1:
            print(A)
            break

