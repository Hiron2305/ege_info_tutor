lens = []
for l_A in range(0, 200 + 1):
    for r_A in range(l_A, 200 + 1):
        flag = 1
        for x in [i / 2 for i in range(0, 150 * 2 + 1)]:
            P = 130 <= x <= 171
            Q = 150 <= x <= 185
            A = l_A <= x <= r_A
            if ((P) <= (((Q) and (not(A))) <= (not(P)))) == 0:
                flag = 0
                break
        if flag == 1:
            lens.append([r_A - l_A])
print(min(lens)) # 0
print(lens)