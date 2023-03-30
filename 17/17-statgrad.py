f = open('Files/17.txt', 'r')
s = f.readlines()

min_1 = 10**10
for i in range(len(s)):
    n = (int(s[i]))
    if str(n)[-1] == str(n)[-2]:
        min_1 = min(n, min_1)
min_1 = min_1**2

maxi = -10**10
sp_main = []
sp = []
for j in range(len(s) - 1):
    if (((int(s[j]))**2) + ((int(s[j+1]))**2)) < min_1:
        if ((int(s[j])) % 7 == 0) or ((int(s[j + 1])) % 7 == 0):
            if ((str(int(s[j]))[-1]) == (str(int(s[j + 1]))[-2])) or ((str(int(s[j]))[-2]) == (str(int(s[j + 1]))[-1])):
                maxi = max(maxi, ((int(s[j])) ** 2 + (int(s[j + 1])) ** 2))
                sp.append(int(s[j]))
                sp.append(int(s[j + 1]))
                sp_main.append(sp)
                sp = []
print(len(sp_main), maxi, sp_main)