# In case when no answer exists, return an array of size two with both values equal to -1, i.e., [-1, -1].
# In case when multiple answers exist, you may return any of them.
# The order of the indices returned does not matter.
# A single index cannot be used twice.

# Time: O(n)
# Space: O(n)
def two_sum_set(arr, target):
    nums = set()
    for _, num in enumerate(arr):
        if target - num in nums:
            return [num, target - num]
        nums.add(num)
    return [-1, -1]


numbers = [2, 3, 5, 7, 1, 0, 5, 9]
target = 10
print(two_sum_set(numbers, target))


# Time: O(n log(n)) for the Tim sort
# Space: O(n)
def two_sum_two_pointers(arr, target):
    arr.sort()  # Now in ascending
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        sum = lo + hi
        if target == sum:
            return [lo, hi]
        elif sum > target:
            hi -= 1
        else:
            lo += 1
    return [-1, -1]


numbers = [2, 3, 5, 7, 1, 0, 5, 9]
target = 10
print(two_sum_set(numbers, target))
