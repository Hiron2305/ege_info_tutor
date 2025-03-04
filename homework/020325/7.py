lens = []
for l_A in range(0, 35 + 1):
    for r_A in range(l_A, 35 + 1):
        flag = 1
        for x in [i / 2 for i in range(0, 25 * 2 + 1)]:
            P = 6 <= x <=  17
            Q = 13 <= x <=  28
            A = l_A <= x <= r_A
            if not(((A) <= (P)) or (Q)):
                flag = 0
                break
        if flag == 1:
            lens.append([r_A - l_A])
print(max(lens))