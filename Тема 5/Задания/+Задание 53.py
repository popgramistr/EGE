# Решение

def to_ter(n):
    n3 = ''
    while n > 0:
        n3 = str(n % 3) + n3
        n = n // 3
    return n3

for n in range(1, 100):
    r = to_ter(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        nd = (n % 3) * 4
        nd = to_ter(nd)
        r = r + nd
    r = int(r, 3)
    print(n, r)

answer = 26

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 53, answer, '4e732ced3463d06de0ca9a15b6153677'))