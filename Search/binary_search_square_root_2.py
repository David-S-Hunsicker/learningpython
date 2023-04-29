class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        left = 0
        right = x + 1
# finds the largest valid answer
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square > x: # all solutions > right are invalid
                right = mid - 1
            else: # square <= x
                left = mid + 1
        return right
s = Solution()
for i in range (1, 11):
    print(str(i) + " Square root " + str(s.mySqrt(i)))