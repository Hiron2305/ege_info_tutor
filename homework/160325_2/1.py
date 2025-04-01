def tick(k, p):
    if (k >= 313) and (p == 2):
        return True
    elif (k < 313) and (p == 2):
        return False
    elif (k >= 313) and (p != 2):
        return False
    else:
        if p % 2 == 0:
            return tick(k + 2, p + 1) and tick(k + 3, p + 1) and tick(k * 3, p + 1)
        else:
            return tick(k + 2, p + 1) or tick(k + 3, p + 1) or tick(k * 3, p + 1)

print([S for S in range(1, 312 + 1) if tick(S, 0)])
#[103, 104]