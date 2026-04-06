# Решение

from ipaddress import ip_network

c = 0
network = ip_network('122.159.136.144/255.255.255.248')
for ip in network:
    if f'{ip:b}'.count('1') % 4 != 0:
        c += 1
print(c)

answer = 5

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1302, answer, 'e4da3b7fbbce2345d7772b0674a318d5'))