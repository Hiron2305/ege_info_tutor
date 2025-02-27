def find_min_n():
    n = 2
    while True:
        binary = bin(n)[2:]
        even_ones = 0
        odd_zeros = 0
        for i in range(len(binary)):
            position = i + 1
            bit = binary[i]
            if position % 2 == 0:
                if bit == '1':
                    even_ones += 1
            else:
                if bit == '0':
                    odd_zeros += 1
        r = abs(even_ones - odd_zeros)
        if r == 5:
            return n
        n += 1

print(find_min_n())