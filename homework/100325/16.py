s = ["*"] * 2040

for i in range(0, 2025):
    if i == 1:
        s[i] = 1
    else:
        s[i] = (i - 1) * s[i - 1]
print((s[2024] + 2 * (s[2023])) / s[2022]) #4094550