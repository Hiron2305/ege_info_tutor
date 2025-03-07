lens = []
for A in range(0, 1000):
    flag = 1
    for x in [i / 2 for i in range(0, 25 * 2 + 1)]:
        f = (int(x) & 94 != 0) <= ((int(x) & 21 == 0) <= (int(x) & A != 0))
        if not(f):
            flag = 0
            break
    if flag == 1:
        lens.append(A)
print(min(lens))