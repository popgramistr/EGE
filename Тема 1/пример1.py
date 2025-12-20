from itertools import permutations

table = '12 15 21 25 26 34 35 43 45 47 51 52 53 54 56 57 62 65 67 74 75 76'
graph = 'АБ АК БА БВ БК ВБ ВГ ВК ГВ ГД ГК ДГ ДЕ ДК ЕД ЕК КА КБ КВ КГ КД КЕ'

for p in permutations('АБВГДЕК'):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)