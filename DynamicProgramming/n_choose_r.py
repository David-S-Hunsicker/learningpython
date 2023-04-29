def ncr(n, r):
    if r == 1 or n == 1:
        return 1
    if r > n:
        return 0

    last = [1]  # 0
    current = [1, 1]  # 1
    if r > n // 2:
        r = n - r
    for row in range(2, n + 1, 1):
        last = current
        current = []
        current.append(1)
        # pascals triangle is symmetric
        # create only half of the values
        for col in range(1, row // 2 + 1, 1):  # 0th val is on line 11
            current.append(last[col] + last[col - 1])
        if row % 2 == 1: # integer division stops generation on odd rows early.
            current.append(current[-1])
    return current[r]


print(ncr(6, 2))
