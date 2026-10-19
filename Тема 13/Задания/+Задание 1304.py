# Решение

def f(x, y, a):
    if x > y:
        if a:
            return 0
        elif x - y == 1:
            return 1
        else:
            return 0
    if x == y:
        return 1
    if a:
        return f(x + 3, y, False) + f(x * 2, y, False)
    else:
        return f(x - 1, y, True) + f(x + 3, y, False) + f(x * 2, y, False)

print(f(3, 12, False))



answer = 53

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1304, answer, 'd82c8d1619ad8176d665453cfb2e55f0'))