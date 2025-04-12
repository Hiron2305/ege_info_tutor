def max_expression_length(s):
    max_len = 0
    n = len(s)
    i = 0

    while i < n:
        if s[i] not in '123456789-':
            i += 1
            continue

        current_value = 0
        pos = i
        sign = 1

        if s[pos] == '-':
            sign = -1
            pos += 1
            if pos >= n or not s[pos].isdigit():
                i += 1
                continue

        if pos >= n or not s[pos].isdigit():
            i += 1
            continue

        num = 0
        start = pos
        while pos < n and s[pos].isdigit():
            num = num * 10 + int(s[pos])
            pos += 1
        current_value = sign * num

        if current_value <= -20000:
            i += 1
            continue

        current_len = pos - i
        if current_len > max_len:
            max_len = current_len

        while pos < n:
            if s[pos] != '-':
                break
            pos_op = pos
            pos += 1
            if pos >= n:
                break

            next_sign = 1
            if s[pos] == '-':
                next_sign = -1
                pos += 1
                if pos >= n or not s[pos].isdigit():
                    break

            if pos >= n or not s[pos].isdigit():
                break

            next_num = 0
            start_next = pos
            while pos < n and s[pos].isdigit():
                next_num = next_num * 10 + int(s[pos])
                pos += 1
            next_value = next_sign * next_num

            current_value -= next_value
            if current_value <= -20000:
                break

            current_len = pos - i
            if current_len > max_len:
                max_len = current_len

        i += 1

    return max_len


with open("24_18.txt", "r") as file:
    s = file.read().strip()

print(max_expression_length(s))