with open("24_15.txt", "r") as file:
    s = file.read().strip()

max_count = 0
current_count = 0
i = 0
n = len(s)

while i <= n - 3:
    triplet = s[i:i+3]
    if triplet in {"NPO", "PNO"}:
        current_count += 1
        max_count = max(max_count, current_count)
        i += 3
    else:
        current_count = 0
        i += 1

print(max_count)