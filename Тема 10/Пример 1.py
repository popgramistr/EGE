from ipaddress import ip_network

# 0-й адрес - адрес сети
print(ip_network('167.66.136.176/255.254.0.0', False)[1])