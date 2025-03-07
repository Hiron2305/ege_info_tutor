res = []
for A in range(0, 500):
    flag = 1
    for x in [i / 2 for i in range(0, 50 * 2 + 1)]:
        for y in [i / 2 for i in range(0, 50 * 2 + 1)]:
            if not(((2 * x + y) != 70) or (x < y) or (A < x)):
                flag = 0
                break
        if flag == 0:
            break
    if flag == 1:
        res.append(A)


print(max(res))