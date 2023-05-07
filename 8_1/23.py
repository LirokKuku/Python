def dist(st, en):
    if st == en:
        return 1
    if st < en:
        return 0
    if st > en:
        return dist(st - 1, en) + dist(st // 2, en)

print(dist(34, 11) * dist(11, 2))