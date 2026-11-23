# Решение
from ipaddress import ip_network

for mask in range(32, -1, -1):
    net = ip_network(f'147.222.222.147/{mask}', False)

answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(10, 1003, answer, '35f4a8d465e6e1edc05f3d8ab658c551'))