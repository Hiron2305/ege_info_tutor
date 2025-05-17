import math

with open("26_9.txt") as f:
    N = int(f.readline())
    data = []
    for _ in range(N):
        parts = list(map(int, f.readline().split()))
        ID = parts[0]
        scores = parts[1:]
        total = sum(scores)
        plus = sum(score for score in scores if score > 0)
        answered = sum(1 for score in scores if score != 0)
        data.append((ID, total, plus, answered))

data.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))

quarter = math.ceil(N / 4)
threshold = data[quarter - 1][1:]

first_not_passed = None
for d in data[quarter:]:
    if d[1:] != threshold:
        first_not_passed = d[0]
        break

if N >= 1700:
    target = data[1699][1:]
    same_count = sum(1 for d in data if d[1:] == target)
else:
    same_count = 0

print(first_not_passed, same_count)
