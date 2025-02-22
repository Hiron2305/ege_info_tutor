r = 0
n = 4
while r != 64   :
    s = "5" + "2" * n
    while ("52" in s) or ("1122" in s) or ("2222" in s):
        if "52" in s:
            s = s.replace("52", '11', 1)
        if "2222" in s:
            s = s.replace("2222", "5", 1)
        if "1122" in s:
            s = s.replace("1122", "25", 1)
    r = sum([int(x) for x in s])
    print(r, n)
    n += 1
