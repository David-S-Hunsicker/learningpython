def can_split(nums, threshold, num_of_sub_arrays):
    total = 0
    count = 1
    for num in nums:
        total += num
        if total > threshold:
            total = num
            count += 1
            if count > num_of_sub_arrays: return False
    return True


def split_array(nums: list, num_of_sub_arrays: int) -> int:
    left = max(nums)  # the minimum sum can't be smaller than this
    right = sum(nums)  # the largest summed sub array can't be larger than everything
    # look for the smallest valid solution
    while left < right:
        mid = left + (right - left) // 2
        if can_split(nums, mid, num_of_sub_arrays):
            right = mid
        else:
            left = mid + 1
    return right


nums = [7, 2, 5, 10, 8]
m = 2
print(split_array(nums, m))
