def guessNumber(n) -> int:
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        g = guess(mid)
        if g == 0:
            return g
        elif g == 1: #1 g is lower than the picked number, so increase the guess
            left = mid + 1
        else:# g is higher than the picked number, decrease the guess
            right = mid - 1
    return 0
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):
    if num == 6: return 0
    if num > 6: return -1
    if num < 6: return 1

n = 10
print(guessNumber(n))