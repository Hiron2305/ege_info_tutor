from ipaddress import *


def check(ip):
    for i in ip:
        i = str(i).split(".")
        if 2 * (bin(int(i[0]))[2:].count("1") + bin(int(i[1]))[2:].count("1")) <= (
                bin(int(i[2]))[2:].count("1") + bin(int(i[3]))[2:].count("1")):
            pass
        else:
            return False
    return True

result = 0
for x in range(0, 255):
    a = ip_network(f"32.0.{x}.5/255.255.240.0", strict=0)
    if check(a):
        result = x
        break

print(result)