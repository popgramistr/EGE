# Решение

"""def f(x, y, n24, n27):
    if x == 24:
        n24 = 1
    if x == 27:
        n27 = 1
    if x == y and n24 + n27 == 1:
        return 1
    if x > y:
        return 0
    return f(x + 1, y, n24, n27) + f(x * 2, y, n24, n27) + f(x * 3, y, n24, n27)
print(f(9, 81, 0, 0))"""

def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)

ab = f(9, 24) * f(24, 81)
bc = f(9, 27) * f(27, 81)
b = f(9, 24) * f(24, 27) * f(27, 81)

print(ab + bc - b)

answer = 142

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1301, answer, 'a8baa56554f96369ab93e4f3bb068c22'))