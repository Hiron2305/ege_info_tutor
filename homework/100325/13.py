import ipaddress

s = ipaddress.ip_network("122.159.136.144/255.255.255.248", 0)
counter = 0
for i in s:
    if bin(int(i))[2:].count("1") % 4 != 0:
        counter += 1
print(counter)

#5