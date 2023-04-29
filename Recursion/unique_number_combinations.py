# Result, Iteration Set Partial
# Recursion Is Super Powerful
def find_combinations(n, k):
    def helper(results, iteration, p):
        if len(p) == k:
            results.append(p[:])
            return
        for i in range(iteration, n + 1):
            p.append(i)
            helper(results, i + 1, p)
            p.pop()

    results = []
    helper(results, 1, [])
    return results
