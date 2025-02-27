from ipaddress import *

a = ip_network("252.67.33.87/255.252.0.0", 0)

counter = 0
for i in a:
    i = str(i).split(".")
    if  2 * (bin(int(i[0]))[2:].count("1") + bin(int(i[1]))[2:].count("1")) < (bin(int(i[2]))[2:].count("1") + bin(int(i[3]))[2:].count("1")):
        counter += 1

print(counter)