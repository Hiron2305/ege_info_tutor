def count_even_odd_digits(n):
    even = 0
    odd = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

def transform_number(n):
    binary = bin(n)[2:]
    for _ in range(3):
        even, odd = count_even_odd_digits(int(binary, 2))
        if even > odd:
            binary += '1'
        elif odd > even:
            binary += '0'
        else:
            if int(binary, 2) % 2 == 0:
                binary += '0'
            else:
                binary += '1'
    return int(binary, 2)

def count_unique_R_in_range(start, end):
    unique_R = set()
    for n in range(1, 10**6):
        R = transform_number(n)
        if start <= R <= end:
            unique_R.add(R)
    return len(unique_R)

start = 876544
end = 1234567899

result = count_unique_R_in_range(start, end)
print(result)