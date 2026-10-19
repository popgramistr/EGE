# Решение

def f(n):
    if n % 2 == 0:
        return f(n // 2) + 3
    elif n % 2 != 0 and n % 3 == 0:
        return f(n // 3) + 2
    elif n % 2 != 0 and n % 3 != 0:
        return 0

for i in range(10000000, 20000000):
    if f(i) == 67:
        print(i)

answer = 18874368

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1601, answer, 'd43416548c620037459b5607111f8eb5'))