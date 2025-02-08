r = 0
n = 1

while r <= 81:
    a = bin(n)[2:]
    if n % 2 == 0:
        a += "01"
    else:
        a += "10"

    r = int(a, 2)
    print(r)
    n += 1