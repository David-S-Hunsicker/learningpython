class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        if len(nums) == 2:
            if nums[0] > nums[1]: return 0
            if nums[1] > nums[0]: return 1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if mid == 0 and nums[mid] > nums[mid + 1] or \
                    mid == len(nums) - 1 and nums[mid] > nums[mid - 1] or \
                    nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1


s = Solution()
# nums = [1,2,1,3,5,6,4]
nums = [6,5,4,3,2,3,2]
print(s.findPeakElement(nums))