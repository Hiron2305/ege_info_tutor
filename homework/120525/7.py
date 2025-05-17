with open("26_7.txt") as f:
    S, N = map(int, f.readline().split())
    important = []
    unimportant = []
    for _ in range(N):
        parts = f.readline().split()
        size = int(parts[0])
        if parts[1] == 'A':
            important.append(size)
        else:
            unimportant.append(size)

important.sort(reverse=True)
transfers = []

for file_size in important:
    placed = False
    for t in transfers:
        if sum(t) + file_size <= S:
            t.append(file_size)
            placed = True
            break
    if not placed:
        transfers.append([file_size])

min_transfers = len(transfers)

unimportant.sort()
used_b_files = [False] * len(unimportant)
b_count = 0

for transfer in transfers:
    used_space = sum(transfer)
    space_left = S - used_space
    for i in range(len(unimportant)):
        if not used_b_files[i] and unimportant[i] <= space_left:
            transfer.append(unimportant[i])
            space_left -= unimportant[i]
            used_b_files[i] = True
            b_count += 1

print(min_transfers, b_count)
