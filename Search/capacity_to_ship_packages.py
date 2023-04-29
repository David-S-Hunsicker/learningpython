'''
A conveyor belt has packages that must be shipped from one port to another within D days.
The i-th package on the conveyor belt has a weight of weights[i].
Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation:
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
'''


def can_fill(weights, days, capacity):
    day = 1
    load = 0
    for weight in range(1, weights + 1):
        if load + weight <= capacity:
            load += weight
        else:
            day += 1
            load = weight
        if day > days: return False
    return True

def min_capacity(weights, days):
    w = weights[-1]
    # binary search the capacity, we know that the sum of all weights will work, get that number down
    # search the solution space and find the smallest capacity that is valid
    # right is a valid answer, so return right and scope it down
    right = sum(weights)
    left = max(weights)
    while left < right:
        mid = left + (right - left)//2
        if can_fill(w, days, mid):
            right = mid
        else:
            left = mid+1
    return right
w = 12
weights = [i for i in range(1, w+1)]
print(min_capacity(weights, 5))
#can_fill(weights, days, capacity)
for i in range(22):
    print(str(i) + " " + str(can_fill(w, 5, i)))