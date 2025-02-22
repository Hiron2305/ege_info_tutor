r = 0
n = 4
while r != 63   :
    s = "5" + "2" * n
    while ("72" in s) or ("522" in s) or ("2222" in s):
        if "72" in s:
            s = s.replace("72", '2', 1)
        if "522" in s:
            s = s.replace("522", "27", 1)
        if "2222" in s:
            s = s.replace("2222", "5", 1)
    r = sum([int(x) for x in s])
    print(r, n)
    n += 1
