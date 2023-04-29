def four_sum(nums, target):
    nums.sort()
    return k_sum(nums, target, 0, 4)


def k_sum(nums, target, start, k):
    if start + k > len(nums) or nums[start] * k > target or nums[-1] * k < target:
        return []
    if k == 2:
        return two_sum(nums, target, start)
    result = []
    for i in range(start, len(nums)):
        if i == start or nums[i] != nums[i - 1]:
            sub_result = k_sum(nums, target - nums[i], i + 1, k - 1)
            for item in sub_result:
                item.insert(0, nums[i])
                result.append(item)
    return result


def two_sum(arr, target, start):
    result = []
    lo = start
    hi = len(arr) - 1
    while lo < hi:
        sum = arr[lo] + arr[hi]
        if sum == target:
            result.append([arr[lo], arr[hi]])
            lo += 1
            hi -= 1
        elif sum < target:
            lo += 1
        else:
            hi -= 1

        if lo > start:
            while lo >= hi and arr[lo] == arr[lo - 1]:
                lo += 1
        if hi < len(arr) - 1:
            while lo <= hi and arr[hi] == arr[hi + 1]:
                hi -= 1
    return result


arr = [0, 0, 1, 3, 2, -1]
target = 3
quads = four_sum(arr, target)

print(quads)
