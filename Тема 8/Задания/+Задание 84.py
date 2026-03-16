# Решение

from itertools import product

a = 0
for p in product('0123456789ABCDEF', repeat = 6):
    p = ''.join(p)
    if p.count('5') > 0:
        if p.count('D') + p.count('E') + p.count('F') == 2:
            if p.lstrip('0') == p and (p.count('DD') == 1 or p.count('DE') == 1 or p.count('DF') == 1 or p.count('ED') == 1 or p.count('EE') == 1 or p.count('EF') == 1 or p.count('FD') == 1 or p.count('FE') == 1 or p.count('FF') == 1):
                a += 1
print(a)

answer = 335241

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 84, answer, '85705f54f8b912d25a2eac2583e7093d'))