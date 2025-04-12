with open("24_5.txt", "r") as file:
    s = file.read().strip()

allowed_chars = {'A', 'B', 'D', 'E', '0', '1', '2', '3'}
filtered_s = [c for c in s if c in allowed_chars]

if not filtered_s:
    print(0)
    exit()

values = []
for char in filtered_s:
    if char in {'A', 'E'}:
        values.append(1)
    elif char in {'B', 'D'}:
        values.append(-1)
    elif char in {'0', '2'}:
        values.append(1)
    elif char in {'1', '3'}:
        values.append(-1)

max_len = 0
prefix_sum = 0
prefix_sums = {0: -1}

for i in range(len(values)):
    prefix_sum += values[i]
    if prefix_sum in prefix_sums:
        current_len = i - prefix_sums[prefix_sum]
        if current_len > max_len:
            max_len = current_len
    else:
        prefix_sums[prefix_sum] = i

print(max_len)