'''
Count the number of inversions in a given array of numbers. A pair (nums[i], nums[j]) is said to form an inversion if nums[i] > nums[j] and i < j.
'''
import bisect


def count_inversions(nums):
    n = len(nums)
    increasing = [nums[0]]
    inversions = 0
    for val in range(1, n):
        if nums[val] >= increasing[-1]:
            increasing.append(nums[val])
        else:
            insertion_point = bisect.bisect_right(increasing, nums[val])
            inversions += len(increasing) - insertion_point
    return inversions


# nums = [3, 6, 1, 7, 2]
nums = [75, 72, 66, 45, 32, 19, 4]
print(count_inversions(nums))
