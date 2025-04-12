file = open("24.txt").read()
count = maximum = 0

unavaliable = ["G", "W", "P"]

for i in range(0, len(file)):
    if file[i] not in unavaliable:
        count += 1
        maximum = max(count, maximum)
    else:
        count = 0
print(maximum, len(file))