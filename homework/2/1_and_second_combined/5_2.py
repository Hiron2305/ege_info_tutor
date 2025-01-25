counter_r = 0

for n in range(100000000, 999999999):
    a = sum([int(x) for x in str(n)])
    b = str(bin(a))[2:]

    if b.count("1") % 2 == 0:
        b = "1" + b + "00"
    else:
        b = "10" + b + "1"

    r = int(b, 2)
    if r == 21:
        counter_r+=1
        print(n, counter_r)

print(counter_r)