import random
def sort(arr, start, end):
    if start >= end:
        return
    # Pick a random element as pivot.
    randindex = random.randint(start, end)
    arr[randindex], arr[start] = arr[start], arr[randindex]
    pivot = arr[start]
    smaller = start
    bigger = start
    for bigger in range(start + 1, end + 1):
        if arr[bigger] <= pivot:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
    arr[start], arr[smaller] = arr[smaller], arr[start]
    sort(arr, start, smaller - 1)
    sort(arr, smaller + 1, end)

def quick_sort(arr):
    sort(arr, 0, len(arr) - 1)
    return arr

l = [5, 2, 1, 3, 4]
print(quick_sort(l))
