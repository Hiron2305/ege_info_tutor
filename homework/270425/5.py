with open('24_5.txt', 'r') as f:
    s = f.read().strip()
n = len(s)
left = 0
countM = 0
ans = 0
for right in range(n):
    if s[right] == 'M':
        countM += 1
    while countM > 278 and left <= right:
        if s[left] == 'M':
            countM -= 1
        left += 1
    ans = max(ans, right - left + 1)
print(ans)
