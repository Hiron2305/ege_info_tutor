with open("24_9.txt", "r") as file:
    s = file.read().strip()

max_length = 0
last_x = -1
last_y = -1
start = 0

for i, char in enumerate(s):
    if char == 'X':
        last_x = i
    elif char == 'Y':
        last_y = i

    if last_x != -1 and last_y != -1:
        current_start = min(last_x, last_y) + 1
        current_length = i - current_start + 1
        max_length = max(max_length, current_length)

print(max_length)