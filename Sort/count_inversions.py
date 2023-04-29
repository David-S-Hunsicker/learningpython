def count_inversions(nums):
    inversions = 0

    def merge(nums, start, mid, end):

        nonlocal inversions
        left = start
        right = mid + 1
        aux = []
        while left <= mid and right <= end:
            if nums[right] < nums[left]:
                aux.append(nums[right])
                inversions += mid - left + 1
                right += 1
            else:
                aux.append(nums[left])
                left += 1
        aux += nums[left:mid+1]
        aux += nums[right:end+1]

        nums[start:end + 1] = aux

    def merge_sort(nums, left, right):
        if left == right: return
        mid = left + (right - left) // 2
        merge_sort(nums, left, mid)
        merge_sort(nums, mid + 1, right)
        merge(nums, left, mid, right)

    merge_sort(nums, 0, len(nums) - 1)
    return inversions

nums = [8,8,8,8]
print(count_inversions(nums))
