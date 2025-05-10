import re
with open('24_4.txt', 'r') as f:
    s = f.read().strip()
n = len(s)
allowed = set('0123456789+-')
max_len = 0
i = 0
while i < n:
    if s[i] not in allowed or s[i] == '+' or s[i] == '-':
        i += 1
        continue
    j = i
    while j < n and s[j] in allowed:
        j += 1
    expr = s[i:j]
    if expr and expr[0].isdigit() and expr[-1].isdigit():
        parts = re.split(r'(\+|\-)', expr)
        valid = True
        for part in parts:
            if part == '+' or part == '-':
                continue
            if not part.isdigit() or int(part) % 5 != 0:
                valid = False
                break
        if valid:
            max_len = max(max_len, len(expr))
    i = j
print(max_len)
