with open('24_2.txt', 'r') as f:
    s = f.read().strip()
max_len = 0
digits12 = set("0123456789AB")
even_digits = set("02468A")
i = 0
n = len(s)
while i < n:
    if s[i] == '0' or s[i] not in digits12:
        i += 1
        continue
    j = i
    while j < n and s[j] in digits12:
        j += 1
    if s[j-1] in even_digits:
        max_len = max(max_len, j - i)
    i = j
print(max_len)
