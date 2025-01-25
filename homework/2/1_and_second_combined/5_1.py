r = 0
n = 2
while r < 5:
    a = str(bin(n))[2:]
    counter_1 = 0
    counter_2 = 0
    for i in a:
        if i == "1" and a.index(i) % 2 == 0:
            counter_1 += 1
        if i == "0" and a.index(i) % 2 == 1:
            counter_2 += 1
    r = abs(counter_2 - counter_1)
    print(r, n)
    n += 1