# Решение

for A in range(10000):
    if all( (y > A) or (152 != (2 * y + 3 * x)) or (A < x) for x in range(1, 100) for y in range(1, 100)):
        print(A)





answer = 30

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1504, answer, '34173cb38f07f89ddbebc2ac9128303f'))