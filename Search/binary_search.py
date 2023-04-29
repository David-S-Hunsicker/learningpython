def binary_search(a: [], target):
    l = 0
    r = len(a) - 1
    while l < r:
        m = l + (r - l) // 2
        if target < a[m]:
            r = m
        else:
            l = m + 1

    return a[l] == target


arr = [1, 2, 3, 5, 7, 8, 9, 11, 15, 17, 19, 23, 25, 28]
no = [40, 50, 4, 10]
for i in range(len(arr)):
    print(binary_search(arr, arr[i]))

for i in range(len(no)):
    print(binary_search(arr, no[i]))
