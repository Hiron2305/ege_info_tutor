file = open("24_7.txt").read()
count = maximum = 0

needed = ["G", "M", "E"]

for i in range(0, len(file) - 3):
    if file[i] == needed[0] and file[i + 2] == needed[1] and file[i + 3] == needed[2]:
        count += 1
print(count, len(file))