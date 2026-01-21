# Решение

R = 0
N = 0
while R != 999:
    N += 1
    N1 = bin(N)[2:]
    N1 = N1.replace('0', 'a').replace('1', '0').replace('a', '1')
    N1 = int(N1, 2)
    R = N - N1
print(R)



answer = 1011

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 5, answer, '7f975a56c761db6506eca0b37ce6ec87'))