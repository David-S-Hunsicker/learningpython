import random


def kth_largest_in_an_array(numbers, k):
    return select_sort(numbers, k - 1)


# descending
def select_sort(arr, k):
    return select(arr, 0, len(arr) - 1, k)


def select(arr, start, end, k):
    if end == start:
        return arr[start]

    random_index = random.randint(start, end)
    arr[random_index], arr[start] = arr[start], arr[random_index]
    pivot = arr[start]
    big = start
    for small in range(start + 1, end + 1):
        if arr[small] >= pivot:
            big += 1
            arr[small], arr[big] = arr[big], arr[small]
    arr[start], arr[big] = arr[big], arr[start]

    if k == big:
        return arr[k]
    elif k < big:
        return select(arr, start, big - 1, k)
    else:
        return select(arr, big + 1, end, k)


arr = [3, 5, 1, 3, 6, 3, 5, 8, 9, 4, 6]
k = 8
print(kth_largest_in_an_array(arr, k))
