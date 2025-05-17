with open("26_4.txt") as f:
    n = int(f.readline())
    passed = []
    failed = {1: [], 2: [], 3: [], 4: []}

    for _ in range(n):
        parts = f.readline().split()
        student_id = int(parts[0])
        grades = list(map(int, parts[1:]))

        num_twos = grades.count(2)

        if num_twos == 0:
            avg = sum(grades) / 4
            passed.append((avg, student_id))
        else:
            failed[num_twos].append(student_id)

passed.sort(key=lambda x: (-x[0], x[1]))

# Формируем рейтинг
rating = [sid for _, sid in passed]
for twos in range(1, 5):
    rating += sorted(failed[twos])

num_scholarship = n // 4

count = 0
last_scholar = None
for sid in rating:
    if any(sid == x[1] for x in passed):
        count += 1
        if count == num_scholarship:
            last_scholar = sid
            break

for sid in rating:
    for twos in [3, 4]:
        if sid in failed[twos]:
            first_many_twos = sid
            break
    else:
        continue
    break

print(last_scholar, first_many_twos)
