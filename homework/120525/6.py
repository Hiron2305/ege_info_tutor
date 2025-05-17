with open("26_6.txt") as f:
    n = int(f.readline())
    prices = [int(f.readline()) for _ in range(n)]

total = sum(prices)

prices.sort(reverse=True)

discount_best = sum(prices[i] / 2 for i in range(5, len(prices), 6))
total_best = total - discount_best

prices.sort()
discount_worst = sum(prices[i] / 2 for i in range(0, len(prices), 6))
total_worst = total - discount_worst

print(total_best, total_worst)
