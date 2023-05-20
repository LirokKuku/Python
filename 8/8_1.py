for p in range(6,100):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                k1 = y*p**2 + 4*p + y
                k2 = y*p**2+6*p+5
                k3 = x*p**3 + z*p**2 + 3*p + 3
                if k1 + k2 == k3:
                    print(x*p**2 + y*p + z)
                    break