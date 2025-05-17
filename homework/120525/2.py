with open('26_2.txt') as f:
    n = int(f.readline())
    events = []

    for _ in range(n):
        start, end = map(int, f.readline().split())
        events.append((start, 1))
        events.append((end, -1))

events.sort()

curr = 0
intervals = []
prev_time = 0

for time, delta in events:
    if time != prev_time:
        intervals.append((prev_time, time, curr))
        prev_time = time
    curr += delta

if prev_time < 1440:
    intervals.append((prev_time, 1440, curr))

change_moments = sorted(set(i[0] for i in intervals[1:]))

max_duration = max(b - a for a, b, _ in intervals)

penultimate_change = change_moments[-2]

print(penultimate_change, max_duration)
