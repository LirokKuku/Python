alf = 'АЛПЦЯ'
k = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    k += 1
                    word = i1 + i2 + i3 + i4 + i5
                    if (word.count('А') <= 1) and (word.count('Ц') == 2) and (word.count('Л') == 0):
                        print(k)
                        print(word)
                        exit()