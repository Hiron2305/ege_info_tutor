from ipaddress import *

a = ip_network("23.140.159.160/255.255.252.0", 0)

counter = 0
for i in a:
    i = str(i).split(".")
    if bin(int(i[0]))[2:].count("1") + bin(int(i[1]))[2:].count("1") >= bin(int(i[2]))[2:].count("1") + bin(int(i[3]))[2:].count("1"):
        counter += 1

print(counter)
