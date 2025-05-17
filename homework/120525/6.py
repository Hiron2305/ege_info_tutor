with open("26_6.txt") as f:
    n = int(f.readline())
    prices = [int(f.readline()) for _ in range(n)]

total = sum(prices)

prices.sort(reverse=True)

discount_best = sum(prices[i] / 2 for i in range(5, len(prices), 6))
total_best = total - discount_best

prices.sort()
group_count = len(prices) // 6
discount_worst = sum(prices[i] // 2 for i in range(group_count))
total_worst = total - discount_worst

print(total_best, total_worst)
