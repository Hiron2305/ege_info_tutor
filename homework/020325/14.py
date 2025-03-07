


def check(x):
    s = ["*"] * 10000
    for i in range(5000, 0, -1):
        if i >= 3000:
            s[i] = i
        else:
            s[i] = i + x + s[i + 2]

    return int(s[2984]) - int(s[2988])

for x in range(-1000, 1000):
    if check(x) == 5916:
        print(x)
        break