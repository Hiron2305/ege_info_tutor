with open("24_10.txt", "r") as file:
    s = file.read().strip()

max_len = 0
current_len = 0
expected = 'number'
has_operator = False
i = 0

while i < len(s):
    if s[i] in {'0', '7', '8', '9'}:
        start = i
        while i < len(s) and s[i] in {'0', '7', '8', '9'}:
            i += 1
        num = s[start:i]
        if len(num) > 1 and num[0] == '0':
            current_len = 0
            expected = 'number'
            has_operator = False
            i = start + 1
            continue
        if expected == 'number':
            current_len += (i - start)
            expected = 'operator'
        else:
            current_len = (i - start)
            expected = 'operator'
            has_operator = False
        i -= 1
    elif s[i] in {'–', '*'}:
        if expected == 'operator':
            current_len += 1
            expected = 'number'
            has_operator = True
            max_len = max(max_len, current_len)
        else:
            current_len = 0
            expected = 'number'
            has_operator = False
    else:
        current_len = 0
        expected = 'number'
        has_operator = False
    i += 1

if has_operator:
    max_len = max(max_len, current_len)

print(max_len)