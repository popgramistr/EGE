# Решение

from itertools import permutations


table = '12 13 14 15 17 21 23 24 31 32 37 41 42 45 51 54 56 65 67 71 73 76'
graph = 'AB AF AG BA BD BE BF BG CD CE DC DB DF EC EB EG FA FB FD GA GB GE'

for p in permutations('ABCDEFG'):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)


answer = 34

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 12, answer, 'e369853df766fa44e1ed0ff613f563bd'))