with open('24_20.txt', 'r') as f:
    s = f.read().strip()


def is_ladder(sub):
    if not sub:
        return False

    n = 1
    i = 0
    while i < len(sub):
        char = sub[i]
        if i + n > len(sub) or not all(sub[i + k] == char for k in range(n)):
            return False
        if n > 1 and char == sub[i - 1]:
            return False
        i += n
        n += 1
    return True


max_len = 0
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]
        if is_ladder(sub):
            max_len = max(max_len, len(sub))

print(max_len)