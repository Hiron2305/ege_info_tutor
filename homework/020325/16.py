s = ["*"] * 2 ** 30
count = 0
for i in range(0, 2 ** 30):
    if i < 2:
        s[i] = i
    else:
        s[i] = s[i//2] + s[i % 2]

    if s[i] == 27:
        count += 1
print(co)