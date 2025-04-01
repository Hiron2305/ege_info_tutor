def f(a, b, p):
    if (a + b) >= 77 and p == 3:
        return True
    elif (a + b) >= 77 and p != 3:
        return False
    elif (a + b) < 77 and p == 3:
        return False

    if p % 2 == 0:
        return f(a + 1, b, p + 1) or f(a * 2, b, p + 1) or f(a, b + 1, p + 1) and f(a, b * 2, p + 1)
    else:
        return f(a + 1, b, p + 1) and f(a * 2, b, p + 1) and f(a, b + 1, p + 1) or f(a, b * 2, p + 1)


print(([S for S in range(1, 69 + 1) if f(7, S, 0)]))