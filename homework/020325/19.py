s = ["*"] * 10000
for i in range(0, 6000):
    if i == 1:
        s[i] = 1
    else:
        s[i] = s[i-1] + i * s[i-1]

print(s[5997] / s[5995])