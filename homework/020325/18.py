s = ["*"] * 10000
for i in range(5000, 0, -1):
    if i >= 2073:
        s[i] = i + 3
    else:
        s[i] = i + s[i+2] + s[i + 3]

print(s[2070] + s[2069])