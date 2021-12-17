import ipaddress

#calcular ips
ip = '192.168.0.1'
endereço = ipaddress.ip_address(ip)
print('Cálculo de IPs: ',endereço+300)

#calcular rede
rede = '192.168.0.0/24'
rede = ipaddress.ip_network(rede)
for ip in rede:
    print('Cálculo de rede: ',ip)