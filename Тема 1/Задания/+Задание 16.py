# Решение
from itertools import permutations

table = '15 18 23 25 35 36 45 47 56 57 58 78 32 51 52 53 54 63 65 74 75 81 85 87'
graph = 'AB AC AD AE AF AG AH BA BC CA CB CD DA DC EA EF FA FE FG GA GF GH HA HG'

print('  1    2    3    4    5    6    7    8')
for p in permutations('ABCDEFGH'):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)
answer = 48

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 16, answer, '642e92efb79421734881b53e1e1b18b6'))