# Решение

from itertools import permutations
print('--1----2----3----4----5----6----7----8--')

table = '13 14 16 23 24 27 28 31 32 34 38 41 42 43 46 56 57 58 61 64 65 67 72 75 76 78 82 83 85 87'
graph = 'АБ АВ АГ АЖ БА БВ БД БИ ВА ВБ ВД ГА ГЕ ГЖ ДБ ДВ ДЕ ДИ ЕГ ЕД ЕИ ЕЖ ИБ ИД ИЕ ИЖ ЖА ЖГ ЖЕ ЖИ'

for p in permutations('АБВГДЕЖИ'):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)

answer = 14

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 10, answer, 'aab3238922bcc25a6f606eb525ffdc56'))