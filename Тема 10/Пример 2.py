from ipaddress import ip_network

for mask in range(32, -1, -1):
    net1 = ip_network(f'202.3.20.24/{mask}', False)
    net2 = ip_network(f'202.3.27.11/{mask}', False)
    if net1 == net2:
        count = 0
        for ip in net1:
            if f'{ip:b}'.count('1') % 2 == 0:
                count += 1
        # print(net1.num_addresses // 2)
        break