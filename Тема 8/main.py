from itertools import product

for line in product('1234', repeat=2):
    print(''.join(line))

print()

for i in '1234':
    for j in '1234':
        print(f'{i}{j}')