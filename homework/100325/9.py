def check(row):
    val_unique = 0
    sum_unique = 0
    sum_repeated = 0

    for i in row:
        if row.count(i) == 1:
            val_unique += 1
            sum_unique += i
        else:
            sum_repeated += i

    if val_unique == 3:
        if sum_repeated ** 2 > sum_unique ** 2:
            return True

    return False





rows = []

with open("9.txt") as file:
    for i in range(25000):
        a = file.readline()
        rows.append([int(x) for x in a.split()])

counter = 0
for row in rows:
    if check(row):
        counter += 1

print(counter)

#273