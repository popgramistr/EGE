# Решение

m = 999999999

for x in range(7):
    for y in range(7):
        a = int(f'{y}{x}320', 7)
        b = int(f'1{x}3{y}3', 9)
        c = a + b
        if c % 181 == 0:
            m = min(m, c // 181)

print(m)

answer = 148

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1402, answer, '47d1e990583c9c67424d369f3414728e'))