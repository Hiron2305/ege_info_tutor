with open("24_13.txt", "r") as file:
    s = file.read().strip()

max_length = 0
current_length = 0
i = 0
n = len(s)

while i <= n - 3:
    c1, c2, c3 = s[i], s[i+1], s[i+2]
    if c1 in {'B', 'C'} and c2 in {'B', 'C'} and c3 == 'A':
        current_length += 3
        max_length = max(max_length, current_length)
        i += 3
    else:
        current_length = 0
        i += 1

print(max_length)