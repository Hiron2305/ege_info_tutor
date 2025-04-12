with open('24_19.txt', 'r') as f:
    s = f.read().strip()

max_count = 0
current_count = 0

for i in range(len(s) - 1):
    pair = s[i:i + 2]
    consonants = {'С', 'D', 'F'}
    vowels = {'А', 'О'}

    if pair[0] in consonants and pair[1] in vowels:
        current_count += 1
    else:
        current_count = 0

    if current_count > max_count:
        max_count = current_count

print(max_count)
