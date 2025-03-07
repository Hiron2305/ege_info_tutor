s = ["*"] * 10001
g = ["*"] * 10001
for i in range(10000,0, -1):
    if i >= 3210:
        s[i] = 1
    else:
        s[i] = s[i + 3] + 7

for i in range(0, 10000 + 1):
    if i < 10:
        g[i] = i
    else:
        g[i] = g[i -3] + 5

print(s[15] - g[3000])