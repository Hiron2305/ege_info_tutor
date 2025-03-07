s = ["*"] * 10000
for i in range(0, 5500 + 1):
    if i < 11:
        s[i] = i
    elif i >= 11 and i % 2 == 0:
        s[i] = 2 * i - 3 + s[i-2]

    elif i >= 11 and i % 2 == 1:
        s[i] = 3 * i - 4 + s[i-3]

print(s[5500] - s[5497])