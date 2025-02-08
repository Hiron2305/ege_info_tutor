def find_N(target):
    for N in range(256):
        inv = 255 - N
        diff = inv - N
        if diff == target:
            return N
    return None

target = 111

N = find_N(target)
print(N)