# In case when no answer exists, return an array of size two with both values equal to -1, i.e., [-1, -1].
# In case when multiple answers exist, you may return any of them.
# The order of the indices returned does not matter.
# A single index cannot be used twice.

def two_sum(arr, target):
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        sum = arr[lo] + arr[hi]
        if sum == target:
            return [[arr[lo], arr[hi]]]
            lo += 1
            hi -= 1
        elif sum < target:
            lo += 1
        else:
            hi -= 1
        # if it wasn't right the first time it won't be right the nth time
        if lo > start:
            while lo >= hi and arr[lo] == arr[lo - 1]:
                lo += 1
        if hi < len(arr) - 1:
            while lo <= hi and arr[hi] == arr[hi + 1]:
                hi -= 1
    return [-1, -1]