def check(a, b, minn):
    if ((a < 0 and b >= 0) or (b < 0 and a >= 0)) and ((a + b > 0) and ((a + b) % minn == 0)):
        return True
    else:
        return False


nums = []

with open("22.txt") as file:
    for i in range(10000):
        a = file.readline()
        nums.append(int(a))

minn = min(abs(x) for x in nums)
counter = 0
max_sum = -10000
for i in range(0, len(nums) - 1):
    if check(nums[i], nums[i + 1], minn):
        counter += 1
        if nums[i] + nums[i + 1] > max_sum:
            max_sum = nums[i] + nums[i + 1]

print(counter, max_sum)

