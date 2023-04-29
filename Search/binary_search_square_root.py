class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        left = 0
        right = x + 1
# finds smallest invalid answer, returns answer-1
        while left < right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square > x:
                right = mid
            else:
                left = mid + 1
        return left-1
s = Solution()
for i in range (1, 11):
    print(str(i) + " Square root " + str(s.mySqrt(i)))