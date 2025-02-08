n = 0
counter = 0
last_r = 0
while counter != 17:
    a = hex(n)[2:]
    if a.count("B") % 2 == 0:
        a = "1" + a
    else:
        a += "1"

    last_r = int(a, 16)
    if len(str(last_r)) == 2:
        counter += 1
    print(last_r)
    n += 1

print(counter)