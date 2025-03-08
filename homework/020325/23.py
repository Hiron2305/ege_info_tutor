def check(a, b, c, maxx):
    if ((("0" not in str(a)) + ("0" not in str(b)) + ("0" not in str(c))) >= 2) and ((a + b + c) < (maxx / 2)):
        return True
    else:
        return False


nums = []

with open("23.txt") as file:
    for i in range(10000):
        a = file.readline()
        nums.append(int(a))

maxx = max(nums)
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

