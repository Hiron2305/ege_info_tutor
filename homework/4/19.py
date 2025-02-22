from math import sqrt

def check(r):
    if r % 2 == 0:
        return r == 2
    d = 3
    while d * d <= r and r % d != 0:
        d += 2
    return d * d > r


r = 0
n = 4
while check(r) == False:
    s = ">" + 39 * "0" + n * "1" + 39 * "2"
    while (">1" in s) or (">0" in s) or (">2" in s):
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)
    r = sum([int(x) for x in s if x != ">"])
    print(r, n)
    n += 1