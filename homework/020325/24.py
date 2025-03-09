def check(a, b, minn, maxx):
    if ((a % 3 == maxx % 3) or (b % 3 == maxx % 3)) and ((a % 7 == minn % 7) or (b % 7 == minn % 7)):
        return True
    else:
        return False


nums = []

with open("24.txt") as file:
    for i in range(9929):
        a = file.readline()
        nums.append(int(a))

minn = min(nums)
maxx = max(nums)
counter = 0
max_sum = -10000
for i in range(0, len(nums) - 1):
    if check(nums[i], nums[i + 1], minn, maxx):
        counter += 1
        if nums[i] + nums[i + 1] > max_sum:
            max_sum = nums[i] + nums[i + 1]

print(counter, max_sum)

