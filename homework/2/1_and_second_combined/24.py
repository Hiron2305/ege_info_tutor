counter = 0

with open("24.txt") as file:
    for i in range(25000):
        a = [int(x) for x in file.readline().split()]


        first_sum = 0
        second_sum = 0
        counter_list = []

        for i in a:
            b = a.count(i)
            counter_list.append(b)
            if b == 3:
                first_sum += i
            else:
                second_sum += i



        if counter_list.count(3) == 3 and counter_list.count(1) == 3 and first_sum ** 2 > second_sum ** 2:
            counter += 1

print(counter)