def check(a, b, c, maxx):
    if (((a % 7 == 0) + (b % 7 == 0) + (c % 7 == 0)) == 2) and (a + b + c) < maxx:
        return True
    else:
        return False


nums = []

with open("23.txt") as file:
    for i in range(6635):
        a = file.readline()
        nums.append(int(a))

maxx = max(x for x in nums if str(x)[-2:] == "09")
counter = 0
max_sum = -10000
for i in range(0, len(nums) - 2):
    a = nums[i]
    b = nums[i + 1]
    c = nums[i + 2]
    if check(a,b,c,maxx):
        counter += 1
        if (a + b + c) > max_sum:
            max_sum = a + b + c

print(counter, max_sum)

