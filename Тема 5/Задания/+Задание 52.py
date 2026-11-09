# Решение

for N in range(1, 100000):
    count_1 = 0
    count_0 = 0
    R = bin(N)[2:]
    for i in range(len(R)):
        if i % 2 == 0 and R[i] == '0':
            count_0 += 1
        elif i % 2 != 0 and R[i] == '1':
            count_1 += 1
    R = abs(count_0 - count_1)
    if R == 5:
        print(N)

answer = 1023

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 52, answer, 'ce5140df15d046a66883807d18d0264b'))