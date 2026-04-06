# Решение

from itertools import permutations

table = '15 16 24 25 26 28 37 38 42 45 47 48 51 52 54 56 61 62 65 73 74 78 82 83 84 87'
graph = 'АБ АГ АЕ БА БГ БЖ БД ВД ВИ ГА ГБ ГЖ ГЕ ДБ ДВ ДИ ДЖ ЕА ЕГ ЖГ ЖБ ЖД ЖИ ИЖ ИД ИВ'

print('1 2 3 4 5 6 7 8')

for p in permutations('АБВГДИЕЖ'):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(*p)

answer = 19

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 15, answer, '1f0e3dad99908345f7439f8ffabdffc4'))