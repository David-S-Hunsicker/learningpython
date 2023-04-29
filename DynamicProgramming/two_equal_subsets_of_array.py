def two_equal_subsets(nums):
    all_sum = sum(nums)
    if all_sum % 2 == 1:
        return False
    t = all_sum // 2
    n = len(nums)
    rows = n
    cols = t+1
    dp = [[False] * cols for _ in range(rows)]

    for i in range(0, rows, 1):
        dp[i][0] = True # It's always possible to get target=0
    for j in range(1, cols, 1):
        dp[0][j] = True if nums[0] == j else False

    for i in range(1, rows, 1):
        cur_num = nums[i]
        for j in range(1, cols, 1):
            exclude = dp[i-1][j]
            include = dp[i-1][j-cur_num] if j-cur_num >= 0 else False
            dp[i][j] = include or exclude
    return dp[-1][-1]

nums = [1, 5, 11, 5]
print(two_equal_subsets(nums))

# purely recursion DFS implementation
# time: 2 ^ n
# space: implicit: n, explicit
# def two_equal_subsets_dfs(nums):
#     sets = set()
#     target = sum(nums)
#     if target % 2 == 1:
#         return False
#     target //= 2
#
#     def dfs(i, target):
#         if target < 0:
#             return
#         if i == len(nums):
#             if target == 0:
#                 return True
#             return False
#         # exclude
#         if helper(i + 1, target):
#             return True
#         # include
#         if helper(i + 1, target - nums[i]):
#             return True
#         return False
#     return dfs(0, target)
#
# nums = [1,5,11,5]
# print(two_equal_subsets_dfs(nums))