def tick(k, p):
    if (k >= 166) and (p == 3):
        return True
    elif (k < 166) and (p == 3):
        return False
    elif (k >= 166) and (p != 3):
        return False
    else:
        if p % 2 == 0:
            avaliable_moves = []
            n = 1
            while (k * n) - k <= 80:
                avaliable_moves.append(n)
                n += 1

            for i in avaliable_moves:
                return tick(k + 2, p + 1) or tick(k * i, p + 1)
        else:
            avaliable_moves = []
            n = 1
            while (k * n) - k <= 80:
                avaliable_moves.append(n)
                n += 1

            for i in avaliable_moves:
                return tick(k + 2, p + 1) or tick(k * i, p + 1)

print(min([S for S in range(1, 300 + 1) if tick(S, 0)]))
#[103, 104]