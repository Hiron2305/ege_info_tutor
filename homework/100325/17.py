nums = []
max_13 = -1000000
with open("17.txt") as file:
    for i in range(6646):
        a = file.readline().rstrip()
        nums.append(int(a))


        if (a[-2:] == "13") and (int(a) > max_13):
            max_13 = int(a)

counter = 0
min_sum = 1000000
for i in range(len(nums) - 2):
    a = nums[i]
    b = nums[i + 1]
    c = nums[i + 2]
    if ((len(str(abs(a))) == 3) + (len(str(abs(b))) == 3) + (len(str(abs(c))) == 3)) == 2:
        if (a + b + c) < max_13:
            counter += 1
            if (a + b + c) < min_sum:
                min_sum = (a + b + c)

print(counter, min_sum) # 909 -92695