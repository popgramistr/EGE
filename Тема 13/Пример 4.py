from ipaddress import ip_network

for mask in range(32, -1, -1):
    net = ip_network(f'68.30.20.77/{mask}', False)
    if f'{net[0]:b}'.count('1') == (32 - mask):
        count = 0
        for ip in net:
            if f'{ip:b}'.count('1') == 10:
                count += 1
        print(count)