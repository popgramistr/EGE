# Решение
from itertools import product

print('x y z w')
for p in product([1, 0], repeat=4):
    x, y, z, w = p
    if not((x <= y or z <= w) and ((z == y) <= (w == x))):
        print(*p)


answer = 'yxwz'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 21, answer, '1ed5bb3720986c091b8dc2704366e53d'))