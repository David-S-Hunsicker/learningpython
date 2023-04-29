import random
def three_partition_sort(arr, start, end):
    if start >= end:
        return
    small = start
    big = end
    pivot = arr[random.randint(start, end)]
    i = start
    while i <= big:
        if arr[i] < pivot and small <= i:
            arr[small], arr[i] = arr[i], arr[small]
            small += 1
        elif arr[i] > pivot and big > i:
            arr[big], arr[i] = arr[i], arr[big]
            big -= 1
        else:
            i += 1
    three_partition_sort(arr, start, small-1)
    three_partition_sort(arr, big, end)

arr = [3,5,1,3,6,3,5,8,9,4,6]
three_partition_sort(arr, 0 , len(arr)-1)
print(arr)