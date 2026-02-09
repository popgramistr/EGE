# Решение

from itertools import product

print('x y z w')
for x, y, z, w in product([1, 0], repeat=4):
    if not((x or not(y)) <= (1 == z)):
        print(x, y, z, w)





answer = 'ywxz'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 11, answer, '7379de4777f5748aa568b8d0bf8c3795'))