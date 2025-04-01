def tick(k, p):
    if (k >= 313) and (p == 4):
        return True
    elif (k < 313) and (p == 4):
        return False
    elif (k >= 313) and (p != 4):
        return False
    elif (k >= 313 and p == 2):
        return False
    else:
        if p % 2 == 0:
            return tick(k + 2, p + 1) and tick(k + 3, p + 1) and tick(k * 3, p + 1)
        else:
            return tick(k + 2, p + 1) or tick(k + 3, p + 1) or tick(k * 3, p + 1)

results = [S for S in range(1, 312 + 1)
           if not tick(S, 1) and tick(S + 2, 2) or tick(S + 3, 2) or tick(S * 3, 2)]
print(sum(results))