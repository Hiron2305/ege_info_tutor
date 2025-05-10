with open('24_6.txt', 'r') as f:
    s = f.read().strip()
vowels = set('AEIOUY')
consonants = set(chr(c) for c in range(65, 91)) - vowels
pattern_positions = []
for i in range(len(s)-2):
    if s[i] in consonants and s[i+1] in consonants and s[i+2] in vowels:
        pattern_positions.append(i)
ans = 0
for k in range(len(pattern_positions)-1):
    start = pattern_positions[k]
    end = pattern_positions[k+1] + 2
    ans = max(ans, end - start + 1)
print(ans)
