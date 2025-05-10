with open('24_9.txt', 'r') as f:
    s = f.read().strip()
pos = []
i = s.find("AB")
while i != -1:
    pos.append(i)
    i = s.find("AB", i+1)

ans = 0
for i in range(len(pos) - 49):
    left_bound = pos[i]
    if i > 0:
        left_bound = pos[i-1] + 2
    if i == 0:
        left_bound = 0
    right_bound = pos[i+49] + 1
    if i+50 < len(pos):
        right_bound = pos[i+50]
    else:
        right_bound = len(s)
    ans = max(ans, right_bound - left_bound)
print(ans)
