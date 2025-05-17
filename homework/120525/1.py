from collections import defaultdict

with open('26_1.txt') as f:
    n = int(f.readline())
    student_tasks = defaultdict(set)
    for line in f:
        student_id, task_id = map(int, line.split())
        student_tasks[student_id].add(task_id)

max_count = 0
best_student = None

for student_id in student_tasks:
    tasks = sorted(student_tasks[student_id])

    max_through_one = 0
    for start in range(2):
        count = 1
        for i in range(start + 2, len(tasks), 2):
            count += 1
        max_through_one = max(max_through_one, count)

    if max_through_one > max_count or (max_through_one == max_count and student_id < best_student):
        max_count = max_through_one
        best_student = student_id

print(best_student, max_count)
