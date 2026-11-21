# Решение
from itertools import product

c = '2468'
nc = '1357'
count = 0

for num in product(c, nc, c, nc, c, nc, c, nc, c, nc, c):
    check = True
    num = ''.join(num)
    for i in range(1, 9):
        if num.count(str(i)) > 4:
            check = False
            break
    if check:
        count += 1

print(count * 2)

answer = 8200800

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 17, answer, 'd67d496249f30f93dd6a7a6d84701d60'))