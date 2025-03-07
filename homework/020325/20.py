s = ["*"] * 10001
for i in range(0, 10000 + 1):
    if i <= 3:
        s[i] = i
    elif i > 3 and i % 2 == 1:
        s[i] = 2 * i + s[i-2]
    elif i > 3 and i % 2 == 0:
        s[i] = i ** 2 + s[i-1]

print(s[10000] - s[9995])