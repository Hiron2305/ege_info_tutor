counter = 0
with open("24_1.txt") as file:
    for i in range(15000):
        a = file.readline()
        if ("Q" in a) and ("W" in a) and ("E" in a) and ("R" in a) and ("T" in a) and ("Y" in a):
            counter += 1
print(counter)