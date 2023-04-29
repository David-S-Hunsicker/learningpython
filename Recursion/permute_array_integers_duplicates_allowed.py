def get_permutations(arr):
    def helper(results, iteration):
        if iteration == len(arr):
            candidate = str(arr)
            if candidate not in seen:
                results.append(arr[:])
                seen.add(candidate)
            return

        for i in range(iteration, len(arr)):
            # if iteration != i and arr[iteration] != arr[i]:
            arr[iteration], arr[i] = arr[i], arr[iteration]
            helper(results, iteration + 1)
            arr[iteration], arr[i] = arr[i], arr[iteration]
        # else:
        #     helper(results, iteration + 1)

    results = []
    seen = set()
    helper(results, 0)
    return list(results)


arr = [6, 6]
print(get_permutations(arr))
