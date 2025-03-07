lens = []
for l_A in range(0, 1000 + 1):
    for r_A in range(l_A, 1000 + 1):
        flag = 1
        for x in [i / 2 for i in range(0, 1000 * 2 + 1)]:
            P = 52 <= x <=  105
            Q = 0 <= x <=  53
            A = l_A <= x <= r_A
            if (((not(P)) and (not(Q)) and (not(A))) <= (x**2 > 303601)) == 0:
                flag = 0
                break
        if flag == 1:
            lens.append([r_A - l_A])
print(min(lens))