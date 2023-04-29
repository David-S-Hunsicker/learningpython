def insertion_sort(list:[]):
    for i in range(1, len(list)):
        temp = list[i]
        j = i-1
        while j >= 0 and temp < list[j]:
            list[j+1] = list[j]
            j-=1
        list[j+1] = temp
    return list



list = [4,3, 2, 1]
print(insertion_sort(list))