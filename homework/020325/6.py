def check(a, b, c):
    return (a * b) > c

res = []
for A in range(-200, 200 + 1):
    flag = 1
    for x in range(1, 200 + 1):
        for y in range(1, 200 + 1):
            if ((not check(x, y, A + 13)) <= (check(28, y, 520) or check(x, 25, 800))) == 0:
                flag = 0
                break
        if flag == 0:
            break
    if flag:
        res.append(A)
print(max(res))
