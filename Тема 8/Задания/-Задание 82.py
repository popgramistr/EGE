# Решение

from itertools import product

n = 0
for p in product('АКОРСТ', repeat = 5):
    n += 1
    line = ''.join(p)
    l = line[0]
    if (l == 'Р' or l == 'О' or l == 'К') and line.count('О') == 2 and n % 2 == 0:
        ans = line
        print(ans, n)

print(ans)

answer = 'РТООТ'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 82, answer, '7ffb4e0ece07869880d51662a2234143'))