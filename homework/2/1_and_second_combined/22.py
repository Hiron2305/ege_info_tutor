from itertools import product

al = "012345678"
counter = 0
for i in product(al, repeat=7):
    if int(i[0]) % 2 == 0 and int(i[-1]) % 3 != 0 and i.count("6") >= 1:
        counter += 1

print(counter)
