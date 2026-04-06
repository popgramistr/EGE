# Решение

s = []

for N in range(1, 1001):
    N2 = bin(N)[2:]
    R = N2 + bin(N % 4)[2:]
    R = int(R, 2)
    s.append(R)

print(set(s))



answer = 19

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 14, answer, '1f0e3dad99908345f7439f8ffabdffc4'))