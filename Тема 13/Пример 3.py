from ipaddress import ip_network

for mask in range(32, -1, -1):
    net1 = ip_network(f'120.91.176.213/{mask}', False)
    net2 = ip_network(f'120.91.174.205/{mask}', False)
    if net1 != net2:
        print(net1.netmask)