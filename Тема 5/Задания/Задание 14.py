# Решение

for N in range(1, 101):
    Nb = bin(N)[2:]
    M = bin(N % 4)[2:]
    R = Nb + M
    R = int(R, 2)
    print(R)





answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 14, answer, '1f0e3dad99908345f7439f8ffabdffc4'))