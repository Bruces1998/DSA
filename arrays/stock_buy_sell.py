def stocks(prices):
    minn = float("inf")
    max_profit = 0

    for price in prices:
        minn = min(minn, price)
        max_profit = max(max_profit, price-minn)

    return max_profit


print(stocks(list(map(int, input("Enter Prices:").split(" ")))))