from itertools import permutations

count = 0
for s in permutations('ОЛЬГА'):
    line = ''.join(s)
    if line[0] != 'Ь' and line.count('ОЬ') == 0 and line.count('АЬ') == 0:
        count += 1
print(count)