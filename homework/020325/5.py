res = []
for A in range(0, 1000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            flag = 1
            f = (not((x < 7) or (y >= (5 * x + A - 60)) or (x >= 36) or (y < 225)))
            if f == 1:
                flag = 0
                break
        if f == 1:
            flag = 0
            break
    if f == 0:
        res.append(A)
print(max(res))