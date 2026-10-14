# Решение

def f(x, y, n24, n27):
    if x == 24:
        n24 = 1
    if x == 27:
        n27 = 1
    if x == y and n24 + n27 == 1:
        return 1
    if x > y:
        return 0
    return f(x + 1, y, n24, n27) + f(x * 2, y, n24, n27) + f(x * 3, y, n24, n27)
print(f(9, 81, 0, 0))

answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1301, answer, 'a8baa56554f96369ab93e4f3bb068c22'))