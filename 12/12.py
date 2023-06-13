for i1 in range(1, 100):
    for i2 in range(1, 100):
        for i3 in range(1, 100):
            s = '0' + '1' * i1 + '2' * i2 + '3' * i3 + '0'
            while '00' not in s:
                s = s.replace('01', '21022', 1)
                s = s.replace('02', '310', 1)
                s = s.replace('03', '230112', 1)
            if s.count('1') == 96 and s.count('2') == 36 and s.count('3') == 80:
                print(len(s))
                exit()