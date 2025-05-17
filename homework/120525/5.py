with open("26_5.txt") as f:
    n = int(f.readline())
    positions = [int(f.readline()) for _ in range(n)]

positions.sort()

max_count = 0
max_first_position = 0

for i in range(n):
    current = positions[i]
    count = 1
    last = current
    for j in range(i + 1, n):
        if positions[j] - last >= 8:
            count += 1
            last = positions[j]
    if count > max_count or (count == max_count and current > max_first_position):
        max_count = count
        max_first_position = current

print(max_count, max_first_position)
