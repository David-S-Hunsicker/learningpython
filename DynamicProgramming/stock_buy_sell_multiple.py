# def get_maximum_profit(prices):
#     maxprofit = 0
#     for i in range(1, len(prices)):
#         if prices[i] > prices[i - 1]:
#             maxprofit += prices[i] - prices[i - 1]
#
#     return maxprofit
#
#
# prices =  [6, 2, 4, 5, 7, 3]
# print(get_maximum_profit(prices))


# buy or sell one share per day.
def maximumProfit(price):
    profit = 0
    highest_sell = price[-1]
    for i in range(len(price)-1, -1, -1):
        if price[i] >= highest_sell:
            highest_sell = price[i]
        else:
            profit += highest_sell - price[i]
    return profit

price = [3,4,5,3,5,2]
print(maximumProfit(price))