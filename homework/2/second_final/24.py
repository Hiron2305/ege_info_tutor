from math import comb

case1 = 4 * comb(8, 2) * (4**2) * (4**8)
case2 = 3 * comb(8, 3) * (4**3) * (4**7)

print(case1 + case2)