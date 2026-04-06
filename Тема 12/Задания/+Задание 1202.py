# Решение

s = bin(145)[2:]
s = s.replace('1', 'I')
s = s.replace('0', '1')
s = s.replace('I', '0')
s += '10'
print(int(s, 2))

answer = 442

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(12, 1202, answer, 'c203d8a151612acf12457e4d67635a95'))