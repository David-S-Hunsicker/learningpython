def binary_search_closest(arr, target):
    n = len(arr)
    left, right = 0, n - 1
    closest_val = float('inf')

    def distance(val):
        return abs(target - val)

    while left <= right:
        mid = (left + right) // 2

        if distance(arr[mid]) < distance(closest_val):
            closest_val = arr[mid]

        if arr[mid] == target:
            return target
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return closest_val


arr = [1, 4, 6, 8, 10, 12]
target = 7
print(binary_search_closest(arr, target))  # Output: 6
