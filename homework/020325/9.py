res = []
for A in range(0, 300 + 1):
    flag = 1
    for x in range(0, 300 * 2 + 1):
        for y in range(0, 300 * 2 + 1):
            if not((x < 7) or (y >= (3 * x + A - 20)) or (x >= 34) or (y < 121)) == 1:
                flag = 0
                break
        if flag == 0:
            break
    if flag == 1:
        res.append(A)


print(max(res))