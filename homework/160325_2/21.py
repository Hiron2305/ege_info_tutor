def f(a, b, p):
    if (a + b) >= 449 and (p == 1 or p == 3):
        return True
    elif (a + b) >= 449 and (p != 1 or p != 3):
        return False
    elif (a + b) < 449 and (p == 3 ):
        return False

    if p % 2 == 0:
        return f(a + 1, b, p + 1) and f(a * 2, b, p + 1) and f(a, b + 1, p + 1) and f(a, b * 2, p + 1)
    else:
        return f(a + 1, b, p + 1) or f(a * 2, b, p + 1) or f(a, b + 1, p + 1) or f(a, b * 2, p + 1)


print(([S for S in range(1, 435 + 1) if f(11, S, 0)]))