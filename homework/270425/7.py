import re

with open('24_7.txt', 'r') as f:
    s = f.read().strip()
max_val = None
n = len(s)
i = 0
while i < n:
    if not s[i].isdigit():
        i += 1
        continue
    j = i
    while j < n and (s[j].isdigit() or s[j] in '+-'):
        j += 1
    expr = s[i:j]
    if expr and expr[0].isdigit() and expr[-1].isdigit() and '++' not in expr and '--' not in expr and '+-' not in expr and '-+' not in expr:
        try:
            val = eval(expr)
            if max_val is None or val > max_val:
                max_val = val
        except Exception:
            pass
    i = j
print(max_val)
