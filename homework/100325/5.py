n = 0
r = 0

while r != 133:
    a = bin(n)[2:]
    while len(a) < 8:
        a = "0" + a

    a1 = list(a)

    for i in range(len(a1)):
        if a1[i] == "0":
            a1[i] = "1"
        else:
            a1[i] = "0"

    a2 = "".join(a1)
    b = int(a2, 2)
    r = b - n
    print(r, n)
    n += 1

    # 61