counter = 0

with open(r"25.txt") as file:
    for i in range(6400):
        a = [int(x) for x in file.readline().split()]

        counter_list = []
        sum_repeated = 0
        counter_repeated = 0
        sum_unique = 0
        counter_unique = 0

        for i in a:
            b = a.count(i)
            if b > 1:
                sum_repeated += i
                counter_repeated += 1
            else:
                sum_unique += i
                counter_unique += 1
            counter_list.append(b)


        if (counter_repeated > 0) and (counter_unique > 0):
            if (sum_unique / counter_unique) < (sum_repeated / counter_repeated):
                counter += 1
print(counter)
