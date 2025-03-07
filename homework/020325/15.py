s = ["*"] * 10000
for i in range(5000, 0, -1):
    if i >= 2025:
        s[i] = i
    else:
        s[i] = i + 3 + s[i + 3]

print(s[2018] - s[2022])