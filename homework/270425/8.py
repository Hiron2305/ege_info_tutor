with open('24_8.txt', 'r') as f:
    s = f.read().strip()
vowels = set('AEIOUY')
consonants = set(chr(c) for c in range(65, 91)) - vowels
pattern_positions = []
for i in range(len(s)-2):
    if s[i] in consonants and s[i+1] in consonants and s[i+2] in vowels:
        pattern_positions.append(i)
ans = float('inf')
for i in range(len(pattern_positions) - 499):
    start = pattern_positions[i]
    end = pattern_positions[i+499] + 2
    ans = min(ans, end - start + 1)
print(ans)
