with open("24_11.txt", "r") as file:
    s = file.read().strip()

max_length = 0
current_length = 0
i = 0

while i < len(s) - 1:
    if s[i] == 'Z' and (s[i+1] in {'X', 'Y'}):
        current_length += 2
        max_length = max(max_length, current_length)
        i += 2
    else:
        current_length = 0
        i += 1

print(max_length)