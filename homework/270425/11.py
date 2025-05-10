with open('24_11.txt', 'r') as f:
    s = f.read().strip()
nop = set('NOP')
max_len = 0
cur_len = 0
prev_is_nop = False
for ch in s:
    if ch in nop:
        if prev_is_nop:
            max_len = max(max_len, cur_len)
            cur_len = 1
        else:
            cur_len += 1
        prev_is_nop = True
    else:
        cur_len += 1
        prev_is_nop = False
    max_len = max(max_len, cur_len)
print(max_len)
