f = open('File/17_2004.txt')
s = [int(x) for x in f.readlines()]

a = []
for i in range(len(s)):
    if s[i] % 13 == 4:
        if s[i] % 8 == 1:
            a.append(s[i])
print(max(a), sum(a))