res = []

for A in range(0, 1000):
    for x in range(0, 100):
        for y in range(0, 100):
            flag = 1
            f = (A > y) or ((3 * x + 2 * y) > 53) or (A > x)
            if f == 0:
                flag = 0
                break
        if flag == 0:
            break
    if flag == 1:
        res.append(A)
print(min(res))
