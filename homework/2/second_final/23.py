from itertools import product


def check(s, a, a2):
    s = "".join(s)
    for i in a + a2:
        if s.count(i) > 4:
            return False
    return True


alph = "135"
alph2 = "2468"
counter = 0


for i in product(alph,alph2, alph,alph2, alph,alph2, alph,alph2, alph,alph2, alph):
    if check(i, alph, alph2):
        counter += 1

print(counter * 2)