def selection_sort(list:[]):

    for i in range(len(list)):
        min = i
        for j in range(i + 1, len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]  # Swap
    return list


list = [-5, -3, -1, 0, 1, 3, 5]
selection_sort(list)
print(list)