import random


def kth_largest(kth_index, initial_stream, append_stream):
    r = []

    def quick_select(arr, k, start, end):
        if start >= end:
            return arr[k]
        rand = random.randint(start, end)
        pivot = arr[rand]
        small = end + 1
        big = start - 1
        i = start
        while i < small:
            if arr[i] > pivot and i > big:
                big += 1
                i += 1
                arr[i], arr[big] = arr[big], arr[i]
            elif arr[i] < pivot:
                small -= 1
                arr[i], arr[small] = arr[small], arr[i]
            else:
                i += 1

        if k == big + 1:
            return arr[k]
        elif k - 1 > small:
            return quick_select(arr, k, small, end)
        else:
            return quick_select(arr, k, start, big - 1)

    for i in range(len(append_stream)):
        initial_stream.append(append_stream[i])
        r.append(quick_select(initial_stream, k - 1, 0, len(initial_stream) - 1))
    return r


k = 2
initial_stream = [1, 1]
append_stream = [2, 3, 4, 5]
print(kth_largest(k, initial_stream, append_stream))
# 1, 2, 3, 4
