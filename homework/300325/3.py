with open("24_2.txt") as file:
    string = file.read()

max_length = current_length = 0

for i in range(len(string)):
    if current_length == 0:
        if string[i] == 'E' or string[i] == 'F':
            current_length = 1
            max_length = max(max_length, current_length)
    else:
        last_char = string[i-1]
        current_char = string[i]
        if (last_char == 'E' and current_char == 'F') or (last_char == 'F' and current_char == 'E'):
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
            if current_char == 'E' or current_char == 'F':
                current_length = 1

print(max_length)