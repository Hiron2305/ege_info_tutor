from ipaddress import *

a = ip_network("142.108.56.118/255.255.255.240", 0)
counter = 0
for i in a:
    i = str(i).split(".")

    if bin(int(i[0]))[2:].count("1") + bin(int(i[1]))[2:].count("1") < bin(int(i[2]))[2:].count("1") + bin(int(i[3]))[2:].count("1"):
        counter += 1

print(counter)