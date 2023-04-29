def merge_sort(list:[]):
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left = list[:middle]  # A colon on the left side of an index means everything before, but not including, the index.
    right = list[middle:]  # A colon on the right side of an index means everything after the specified index.
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result