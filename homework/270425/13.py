with open('24_13.txt', 'r') as f:
    s = f.read().strip()
D_pos = [i for i, ch in enumerate(s) if ch == 'D']
O_pref = [0]
for ch in s:
    O_pref.append(O_pref[-1] + (1 if ch == 'O' else 0))

ans = 0
for i in range(len(D_pos)):
    for j in range(i+1, len(D_pos)):
        d_i = D_pos[i]
        d_j = D_pos[j]
        numO = O_pref[d_j] - O_pref[d_i+1]
        if numO <= 2:
            ans = max(ans, d_j - d_i + 1)
print(ans)
