def most_profit(prices):
    best_sell_price = prices[1]
    best_buy_price = prices[0]
    for i in range(1,len(prices)):
        best_buy_price = min(best_buy_price, prices[i-1])
        best_sell_price = max(best_sell_price, prices[i])
    profit = best_sell_price - best_buy_price
    return profit if profit > 0 else -1

prices = [2, 3, 10, 6, 4, 8, 1]
print(most_profit(prices))