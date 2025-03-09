res = []
for A in range(1, 1000):
    for x in range(1, 1000):
        flag = 1
        f = (((A + x) < 123) <= ((x % 5 == 0) <= (not(x % 7 == 0))))
        if f == 0:
            flag = 0
            break
    if f == 1:
        res.append(A)
print(min(res))