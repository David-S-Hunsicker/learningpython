import random

def select(arr, start, end, k):
    if start >= end:
        return arr[k]
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
    if k >= small and k < big:
        return arr[k]
    elif k < small:
        return select(arr, start, small - 1, k)
    else:
        return select(arr, big, end, k)


def quick_select(arr, k):
    return select(arr, 0, len(arr) - 1, k - 1)


def kth_smallest(arr, k):
    return quick_select(arr, k)


arr = [3, 5, 1, 3, 6, 3, 5, 8, 9, 4, 6]
k = 8
print(quick_select(arr, k))
