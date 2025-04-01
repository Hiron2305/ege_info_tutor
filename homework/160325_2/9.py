def tick(a, b, p):
    if (a + b >= 68) and ((p == 4) or (p == 2)):
        return True
    elif (a + b < 68) and (p == 3):
        return False
    elif (a + b >= 68) and (p != 3):
        return False
    else:
        if p % 2 == 0:
            return tick(a + 1, b, p + 1) and tick(a, b + 1, p + 1) and tick(a + b, b, p + 1) and tick(a, b + a, p + 1)
        else:
            return tick(a + 1, b, p + 1) or tick(a, b + 1, p + 1) or tick(a + b, b, p + 1) or tick(a, b + a, p + 1)

print(([S for S in range(1, 59 + 1) if tick(8, S, 0)]))



def tick(a, b, p):
    if (a + b >= 68) and (p == 2):
        return True
    elif (a + b < 68) and (p == 2):
        return False
    elif (a + b >= 68) and (p != 2):
        return False
    else:
        if p % 2 == 0:
            return tick(a + 1, b, p + 1) and tick(a, b + 1, p + 1) and tick(a + b, b, p + 1) and tick(a, b + a, p + 1)
        else:
            return tick(a + 1, b, p + 1) or tick(a, b + 1, p + 1) or tick(a + b, b, p + 1) or tick(a, b + a, p + 1)

print(([S for S in range(1, 59 + 1) if tick(8, S, 0)]))