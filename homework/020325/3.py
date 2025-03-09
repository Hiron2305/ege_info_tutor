res = []
for A in range(1, 1000):
    for x in range(1, 1000):
        flag = 1
        f = (((x % 3 == 0) <= (not(x % 5 == 0))) or ((x + A) >= 90))
        if f == 0:
            flag = 0
            break
    if f == 1:
        res.append(A)
print(min(res))