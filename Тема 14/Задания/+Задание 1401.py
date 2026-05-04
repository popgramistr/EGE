# Решение

s = '0123456789ABC'
m = 10 ** 99

for x in s:
    for y in s:
        num13 = f'8{x}78{y}'
        num18 = f'79{x}{y}7'
        a = int(num13, 13) + int(num18, 18)
        if a % 9 == 0 and a < m:
            m = a
            xmin = x
            ymin = y
print(m, xmin, ymin)

ans = m // 9
print(ans)

answer = 113024

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1401, answer, '436fc6a87245490c1c09148823eec9ff'))