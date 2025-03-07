res = []
for A in range(1, 1000):
    flag = 1
    for x in range(1, 100):
        if ((x % A != 0) <= ((x % 35 == 0) <= (x % 10 == 0))) == 0:
            flag = 0
            break
    if flag == 1:
        res.append(A)
print(max(res))