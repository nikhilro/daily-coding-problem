def max_profit_naive(prices): # O(n^2) time, O(1) space
    return max(sell - buy for i, buy in enumerate(prices) for sell in prices[i + 1:])

print(max_profit_naive([9, 11, 8, 5, 7, 10]))

def max_profit_gen(prices): # O(n) time, O(1) space
    def min_buy():
        prev = prices[0]
        for price in prices:
            prev = min(prev, price)
            yield prev

    buy = min_buy()
    return max(sell - next(buy) for sell in prices)

print(max_profit_gen([9, 11, 8, 5, 7, 10]))

def max_profit(prices): # O(n) time, O(1) space
    max_profit, prev_min_buy = 0, prices[0]
    for price in prices:
        max_profit = max(price - prev_min_buy, max_profit)
        prev_min_buy = min(price, prev_min_buy)

    return max_profit

print(max_profit([9, 11, 8, 5, 7, 10]))
