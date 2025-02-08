from itertools import product, repeat

alph = "РЕГИНА"
counter = 0

for i in product(alph, repeat=5):
    if i.count("Р") == 1 and i.count("Г") == 1 and (i.count("Н") == 1 or i.count("Н") == 0):
        counter += 1

print(counter) #1080