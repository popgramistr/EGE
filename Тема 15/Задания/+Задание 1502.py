# Решение

p = range(19, 84)
q = range(4, 51)

md = 99999999999

for start in range(100):
    for end in range(100):
        a = range(start, end)
        if all( (x in q) <= ( (not (x in p)) <= ( not ((x in q) and (not (x in a))) ) ) for x in range(100)):
            md = min(md, end - start)
print(md)

answer = 15

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1502, answer, '9bf31c7ff062936a96d3c8bd1f8f2ff3'))