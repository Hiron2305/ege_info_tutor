
r = 0
n = 4
while r != 27:
    s = "3" + "5" * n
    while ("25" in s) or ("355" in s) or ("555" in s):
        if "25" in s:
            s = s.replace("25", '3', 1)
        if "355" in s:
            s = s.replace("355", "52", 1)
        if "555" in s:
            s = s.replace("555", "23", 1)
    r = sum([int(x) for x in s])
    print(r, n)
    n += 1
