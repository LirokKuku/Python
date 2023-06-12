s = '1' * 4 + '3' * 3 + '2' * 2
while '133' in s or '221' in s or '23' in s:
    if '133' in s:
        s = s.replace('133', '1', 1)
    if '221' in s:
        s = s.replace('221', '31', 1)
    if '23' in s:
        s = s.replace('23', '21', 1)
print(s)