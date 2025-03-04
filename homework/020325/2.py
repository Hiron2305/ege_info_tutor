res = []
for A in range(0, 1000):
    for x in range(0, 1000):
        flag = 1
        f = (x & 57 == 0) or ((x & 23 == 0) <= (not(x & A == 0)))
        if f == 0:
            flag = 0
            break
    if flag == 1:
        res.append(A)

print(min(res))