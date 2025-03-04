def check(a, b, c):
    return (a * b) > (2 * c)

res = []
for A in range(-1000, 1000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            flag = 1
            f = (not(check(x, y, A + 13)) <= check(28, y, 520) or check(x, 25, 800))
            if f == 0:
                flag = 0
                break
        if f == 0:
            flag = 0
            break
    if f == 1:
        res.append(A)
print(max(res))