# Решение

def f(x, y):
    if x == y:
        return 1
    if x < y or x == 12 or x == 15:
        return 0
    return f(x - 1, y) + f(x / 2, y) + f(x / 3, y)
print(f(19, 1))

answer = 43

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1303, answer, '17e62166fc8586dfa4d1bc0e1742c08b'))