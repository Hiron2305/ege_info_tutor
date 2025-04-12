with open("24_6.txt", "r") as file:
    s = file.read().strip()

pattern = ['V', 'W', 'X', 'Y', 'Z']
max_length = 0
n = len(s)

for i in range(n - 4):
    if (s[i] == pattern[0] and
            s[i + 1] == pattern[1] and
            s[i + 2] == pattern[2] and
            s[i + 3] == pattern[3] and
            s[i + 4] == pattern[4]):

        left = 0
        current = i - 1
        expected = pattern[-1]
        while current >= 0:
            if s[current] == expected:
                left += 1
                current -= 1
                idx = pattern.index(expected)
                expected = pattern[(idx - 1) % 5]
            else:
                break

        right = 0
        current = i + 5
        expected = pattern[0]
        while current < n:
            if s[current] == expected:
                right += 1
                current += 1
                idx = pattern.index(expected)
                expected = pattern[(idx + 1) % 5]
            else:
                break

        total_length = left + 5 + right
        if total_length > max_length:
            max_length = total_length

print(max_length)