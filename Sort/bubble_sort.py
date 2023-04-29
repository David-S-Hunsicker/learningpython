def bubble_sort(list):
    for i in range(len(list)):
        swapped = False
        for j in range(len(list)-1, i+1, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
                swapped = True
        if not swapped:
            return list

list = [3, 9, -4, 2]
print(bubble_sort(list))