def count_all_subsets(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    odd = 1
    if n % 2 == 1:
        odd = 2
    root = count_all_subsets(n//2)
    return odd * root * root


print(count_all_subsets(8))
