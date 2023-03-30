def is_sim(n):
    check = True
    for d in range(2, n):
        if n % d == 0:
            check = False
            break
    return check


ans = 169
count = 0
while not is_sim(ans):
    ans += 1
    count += 1
print(count)