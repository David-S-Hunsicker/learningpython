class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # returns the index of the lowest value of the array
        def find_pivot(nums):
            left = 0
            right = len(nums) - 1

            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left

        pivot_index = find_pivot(nums)  # the small val in the array
        if target >= nums[pivot_index] and target <= nums[len(nums) - 1]:  # right side
            left = pivot_index
            right = len(nums) - 1
        else:
            left = 0
            right = pivot_index - 1

        # standard binary search, Find the INDEX
        while left <= right:
            index = left + (right - left) // 2
            if nums[index] == target:
                return index
            elif target > nums[index]:
                left = index + 1
            else:
                right = index
        return -1

s = Solution()
nums, target = [3, 1], 1
print(s.search(nums, target))
