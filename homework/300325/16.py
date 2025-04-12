with open('24_16.txt', 'r') as f:
    s = f.read().strip()

if not s:
    print(0)
else:
    max_len = 1
    current_len = 1
    for i in range(1, len(s)):
        prev, curr = s[i-1], s[i]
        if (prev, curr) in {('P', 'R'), ('R', 'P')}:
            current_len = 1
        else:
            current_len += 1
        if current_len > max_len:
            max_len = current_len
    print(max_len)
