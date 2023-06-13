from itertools import permutations

ss = set()
for i in permutations("АМФИБРАХИЙ"):
    s = "".join(i)
    if "ИА" in s or "АА" in s or "АИ" in s or "ИИ" in s: ss.add(i)
print(len(ss))