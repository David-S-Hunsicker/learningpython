def find_top_k_frequent_elements(arr, k):
    num_freq = {}
    result = []
    for i in range(len(arr)):
        if arr[i] not in num_freq:
            num_freq[arr[i]] = 0
        num_freq[arr[i]] += 1
    num_freq = sorted(num_freq.items(), key=lambda x: -x[1])
    for i in range(k):
        result.append(num_freq[i][0])
    return result

arr = [1, 2, 3, 2, 4, 3, 1]
k = 2
print(find_top_k_frequent_elements(arr, k))