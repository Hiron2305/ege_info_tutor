with open('24_10.txt', 'r') as f:
    s = f.read().strip()
pos = []
i = s.find("RO")
while i != -1:
    pos.append(i)
    i = s.find("RO", i+1)

ans = 0
for idx in range(len(pos) - 20):
    start = pos[idx]
    end = pos[idx+20] + 1
    left = start
    while left > 0 and s[left-1] != 'O':
        left -= 1
    if idx+21 < len(pos):
        right = pos[idx+21]
    else:
        right = len(s)
    fragment = s[left:right]
    if "0RO" not in fragment and "ROR" not in fragment:
        ans = max(ans, len(fragment))
print(ans)