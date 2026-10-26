# Решение
"""ans = 0
for n in range(765432015, 1542613240):
    if n % 10 == 9:
        ans += 1
print(ans)"""

answer = 77718123

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1603, answer, '383d228fc45e55c06236b5d6278e1765'))