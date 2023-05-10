def binary_search(a: [], target):
    left = 0
    right = len(a) - 1
    while left < right:
        m = left + (right - left) // 2
        if target < a[m]:
            right = m
        else:
            left = m + 1

    return a[left] == target


arr = [1, 2, 3, 5, 7, 8, 9, 11, 15, 17, 19, 23, 25, 28]
no = [40, 50, 4, 10]
for i in range(len(arr)):
    print(binary_search(arr, arr[i]))

for i in range(len(no)):
    print(binary_search(arr, no[i]))
