from math import sqrt
def check(a, b, c, maxx):
    if ((a >= 0 and (sqrt(a) == int(sqrt(a))) + (b >= 0 and sqrt(b) == int(sqrt(b))) + (c >= 0 and sqrt(c) == int(sqrt(c)))) == 1):
        if (a >= 0 and (sqrt(a) == int(sqrt(a)))) and ((b + c) >= maxx):
            return True
        elif (b >= 0 and sqrt(b) == int(sqrt(b))) and ((a + c) >= maxx):
            return True
        elif (c >= 0 and sqrt(c) == int(sqrt(c))) and ((a + b) >= maxx):
            return True
        else:
            return False


nums = []

with open("26.txt") as file:
    for i in range(5000000):
        a = file.readline()
        nums.append(int(a))

maxx = max(x for x in nums)
counter = 0
max_sum = 0
for i in range(0, len(nums) - 2):
    a = nums[i]
    b = nums[i + 1]
    c = nums[i + 2]
    if check(a,b,c,maxx):
        counter += 1
    if (a >= 0 and (sqrt(a) == int(sqrt(a)))):
        max_sum += a
    elif (b >= 0 and sqrt(b) == int(sqrt(b))):
        max_sum += b
    elif (c >= 0 and sqrt(c) == int(sqrt(c))):
        max_sum += c


print(counter, max_sum)

