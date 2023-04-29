def find_closest_triplet_sum(target, numbers):
    n = len(numbers)
    numbers.sort()
    closest_sum = abs(numbers[0] + numbers[1] + numbers[2])
    def binary_search(arr, left, right, x):
        while left <= right:
            mid = left + (right - left)//2
            if x < arr[mid]: right = mid
            else: left = mid + 1
        return left

    for i in range(n - 2):
        for j in range(i+1, n - 1):
            complement = target - (numbers[i] + numbers[j])
            left = j + 1
            right = n - 1 # last
            closest_num = binary_search(numbers, left, right, complement)


    return closest_sum

target = 9
numbers = [2,2,3,8]
assert(find_closest_triplet_sum(target, numbers) == 7)