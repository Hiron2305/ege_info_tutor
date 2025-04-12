max_distance = 0

with open("24_14.txt", "r") as file:
    for line in file:
        line = line.strip()
        a_count = line.count('A')
        if a_count >= 25:
            continue

        char_indices = {}
        for idx, char in enumerate(line):
            if char == 'A':
                continue
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(idx)

        current_max = 0
        for indices in char_indices.values():
            if len(indices) >= 2:
                distance = indices[-1] - indices[0]
                current_max = max(current_max, distance)

        max_distance = max(max_distance, current_max)

print(max_distance)