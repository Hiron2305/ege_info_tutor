from itertools import product


def check(s, a):
    for i in range(len(s) - 1):
        if int(s[i]) % 2 == int(s[i + 1]) % 2:
            return False
    for i in a:
        if s.count(i) > 3:
            return False

    return True


a = "12345678"
counter = 0
for i in product(a, repeat = 9):
    if check(i, a):
        counter += 1

print(counter)

# 483840