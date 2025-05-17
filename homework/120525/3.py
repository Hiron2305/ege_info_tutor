with open("26_3.txt") as f:
    n, m, k = map(int, f.readline().split())

    occupied = dict()
    for _ in range(n):
        row, seat = map(int, f.readline().split())
        if row not in occupied:
            occupied[row] = set()
        occupied[row].add(seat)

for row in range(m, 0, -1):
    seats = occupied.get(row, set())
    for seat in range(1, k):
        if seat not in seats and seat + 1 not in seats:
            if all(s not in seats for s in range(1, seat)):
                print(row, seat)
                exit()
