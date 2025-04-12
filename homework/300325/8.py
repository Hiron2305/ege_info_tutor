with open("24_8.txt", "r") as file:
    s = file.read().strip()

n = len(s)
max_length = 0
dp_EA = 0
dp_NPC = 0

i = 0
while i < n:
    if i + 1 < n and s[i] == 'E' and s[i+1] == 'A':
        new_dp_EA = max(dp_EA, dp_NPC) + 2
        new_dp_NPC = dp_NPC
        current_max = max(new_dp_EA, new_dp_NPC)
        max_length = max(max_length, current_max)
        dp_EA, dp_NPC = new_dp_EA, new_dp_NPC
        i += 2
    elif i + 2 < n and s[i] == 'N' and s[i+1] == 'P' and s[i+2] == 'C':
        new_dp_NPC = max(dp_EA, dp_NPC) + 3
        new_dp_EA = dp_EA
        current_max = max(new_dp_EA, new_dp_NPC)
        max_length = max(max_length, current_max)
        dp_EA, dp_NPC = new_dp_EA, new_dp_NPC
        i += 3
    else:
        dp_EA = 0
        dp_NPC = 0
        i += 1

if max_length >= 2 or max_length >= 3:
    print(max_length)
else:
    print(0)