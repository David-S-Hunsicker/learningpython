def find_zero_sum(arr):
    arr.sort()  # sort allows for 2 pointer solution which is linear
    trips = set()  # duplicates are disallowed
    for i in range(len(arr) - 2):
        two_sum(i, i + 1, len(arr) - 1, trips, arr)  # linear two pointer sum check
    return list(trips)


def two_sum(first, start, end, trips, arr):
    while start < end:
        sum = arr[first] + arr[start] + arr[end]
        if sum == 0:
            trips.add(str(arr[first]) + "," + str(arr[start]) + "," + str(arr[end]))
        if sum > 0:
            end -= 1
        else:
            start += 1

# Time: O(n^2)
# Space: Theta(n) -> TimSort uses merge sort which uses n space
# Improvements: We could use a quicksort instead to conserve space to n space since data is primitive.


data = [-2, 2, 0, -1, 1]
print(find_zero_sum(data))
