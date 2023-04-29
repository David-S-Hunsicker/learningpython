def max_product(n):
    dp = [0] * (n+1)
    for i in range(2, n+1):
        for cut in range(1, i):
            dp[i] =  max(dp[i], (i-cut) * cut, dp[i-cut] * cut)
    return dp[-1]

print(max_product(6))