# Решение

for N in range(1, 100000):
    count_1 = 0
    count_0 = 0
    R = bin(N)[2:]
    R = abs(R[::2].count('0') - R[1::2].count('1'))
    if R == 5:
        print(N)
answer = 1023

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 52, answer, 'ce5140df15d046a66883807d18d0264b'))