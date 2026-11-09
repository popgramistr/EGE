# Решение
print("y-z")
for y in range(2):
    for z in range(2):
        if not( ( 1 == (y <= z) ) and ( y == (not(z <= 1)) ) ):
            print(y, z)

answer = "wzxy"

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 22, answer, 'c5e4e768af58cf865c4006af69319e62'))