def tick(k, p):
    if k == 1:
        return p % 2 == 1
    if p == 3:
        return False

    moves = []
    if k % 2 == 0:
        moves.append(tick(k // 2, p + 1))
    else:
        if k > 2:
            moves.append(tick(k - 2, p + 1))

    if k % 3 == 0:
        moves.append(tick(k - 2 * (k // 3), p + 1))
    else:
        if k > 3:
            moves.append(tick(k - 3, p + 1))

    if p % 2 == 0:
        return any(moves)
    else:
        return all(moves)


values = [S for S in range(2, 38) if
          any(tick(move, 1) and tick(move, 2) for move in [S // 2, S - 2, S - 3] if move > 0)]
print(min(values) if values else 0)
