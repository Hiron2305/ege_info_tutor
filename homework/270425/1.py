with open('24_1.txt', 'r') as f:
    s = f.read().strip()
positions = []
i = s.find("RSQ")
while i != -1:
    positions.append(i)
    i = s.find("RSQ", i+1)

ans = float('inf')
for i in range(len(positions) - 129):
    start = positions[i]
    end = positions[i+129] + 3
    while end < len(s) and s[end-1] == 'Q':
        end += 1
    ans = min(ans, end - start)
print(ans)
