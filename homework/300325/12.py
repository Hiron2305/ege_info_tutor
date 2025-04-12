with open("24_12.txt", "r") as file:
    s = file.read().strip()

max_length = 1
current_max = 1
prev_char = s[0] if s else ''

for i in range(1, len(s)):
    current_char = s[i]
    if (prev_char == 'N' and current_char == 'P') or (prev_char == 'P' and current_char == 'O'):
        current_max = 1
    else:
        current_max += 1
    max_length = max(max_length, current_max)
    prev_char = current_char

print(max_length)