def coin_change(coins: list[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)  # upper bound
    dp[0] = 0

    # for every amount from 1 to $amount, calculate the shortest way to get there
    # this requires testing every coins value by subtracting it from the desired amount,
    # then with that new amount we just got, check how many coins it took to get that.
    # as we go through the array it will build out all of the answers
    # this also feels like pathing or minimum cost path
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:  # valid calculation
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != amount + 1 else  -1


print(coin_change([1,3,4,5], 9))