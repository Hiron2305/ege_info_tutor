#18 236, 1825
#19 337 1119
#20 1026 1099
#21 964 2735
#22 -363
#23 80


nums = []
with open("23.txt") as file:
    for i in range(500):
        a = float(file.readline().split()[0])
        nums.append(a)

print(nums)
max_sum = -10000
for i in range(len(nums) - 1):
    current_sum = 0
    n = 0
    flag = 0
    while (i + n < len(nums) - 1) and abs(nums[i + n] - nums[i + n + 1]) < 10:
        current_sum += nums[i + n + 1]
        n += 1
        flag = 1
    if flag == 1:
        current_sum += nums[i]
        if current_sum > max_sum:
            max_sum = current_sum


print(max_sum)
