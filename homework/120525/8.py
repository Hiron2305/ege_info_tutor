with open("26_8.txt") as f:
    first_line = f.readline().split()
    N, K, M = map(int, first_line)
    prices = [int(f.readline()) for _ in range(N)]

prices.sort(reverse=True)

discount_20 = prices[:K]
discount_10 = prices[K:K+M]
no_discount = prices[K+M:]

if no_discount:
    max_no_discount = no_discount[0]
else:
    max_no_discount = 0

total_discount = 0
for p in discount_20:
    total_discount += p * 0.20
for p in discount_10:
    total_discount += p * 0.10

print(max_no_discount, int(total_discount))
