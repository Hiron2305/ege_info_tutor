def tick(k, p):
    if (k == 1) and (p == 2):
        return True
    elif (k > 1) and (p == 2):
        return False

    if k % 2 == 0:
        move1 = tick(k // 2, p + 1)
    else:
        move1 = tick(k - 2, p + 1) if k > 2 else False

    if k % 3 == 0:
        move2 = tick(k - 2 * (k // 3), p + 1)
    else:
        move2 = tick(k - 3, p + 1) if k > 3 else False

    if p % 2 == 0:
        return move1 or move2
    else:
        return move1 and move2

print(max([S for S in range(2, 38) if not tick(S, 0) and tick(S, 1)]))
