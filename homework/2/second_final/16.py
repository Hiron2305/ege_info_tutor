def func(n):
    if n == 0:
        return "0"
    answ = ""
    while n > 0:
        answ += str(n % 3)
        n = n // 3
    return answ[::-1]

N = 1
r = 0

func(29)

while len(str(r)) < 4:
    a = func(N)
    a += str(N % 3)
    r = int(a, 3)
    print(r)
    N += 1