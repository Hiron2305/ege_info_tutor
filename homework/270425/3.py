import re

with open('24_3.txt', 'r') as f:
    text = f.read().strip()
pattern = re.compile(r'\b[A-Z][a-z]*'
                     r'(?: [A-Z]?[a-z]+)*\.')
matches = pattern.findall(text)
ans = 0
for match in matches:
    if '  ' in match:
        continue
    valid = True
    for word in match[:-1].split():
        if any(c.isupper() for c in word[1:]):
            valid = False
            break
    if valid:
        ans = max(ans, len(match) - 1)
print(ans)
