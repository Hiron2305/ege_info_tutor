def first_check(row):
    for i in row:
        if row.count(i) >= 3:
            return True
    return False

def second_check(row):
    for i in row:
        if row.count(i) == 1:
            return True
    return False

def third_check(row):
    list_repeated = []
    list_unique = []
    for i in row:
        if row.count(i) == 1:
            list_unique.append(i)
        else:
            list_repeated.append(i)

    avg_repeated = sum(list_repeated) / len(list_repeated)
    avg_unique = sum(list_unique) / len(list_unique)

    if avg_repeated > avg_unique:
        return True
    else:
        return False

rows = []
counter = 0


with open("26.txt") as file:
    for i in range(30000):
        rows.append([int(x) for x in file.readline().split()])

for i in rows:
    if first_check(i) and second_check(i) and third_check(i):
        counter += 1

print(counter)