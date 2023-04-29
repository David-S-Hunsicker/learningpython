import random
def k_most_frequent(k, words):
    word_count = {}
    r = []
    for word in words:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    r = sorted(word_count.items(), key=lambda w: (-w[1], w[0]))

    for i in range(len(r)):
        r[i] = r[i][0]
    return r[:k]

def quick_sort(a, start, end, k):
    if start >= end:
        return

    random_index = random.randint(start, end)
    pivot = a[random_index][1]
    a[random_index], a[start] = a[start], a[random_index]
    smaller = start

    for bigger in range(start + 1, end + 1):
        if a[bigger][1] <= pivot:
            a[bigger], a[smaller] = a[smaller],a[bigger]
            smaller += 1
    a[start], a[smaller] = a[smaller], a[start]
    quick_sort(a, start, smaller-1, k)
    if k > pivot:
        quick_sort(a, smaller+1, end, k)


words = ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare", "taxi"]
k = 4
print(k_most_frequent(k, words))