
def get_permutations(arr):

    return generate(arr, [], [])
def generate(arr, cur, result):
    if len(arr) == 0:
        result.append(list(cur))

    for i in range(len(arr)):
        cur.append(arr.pop(i))
        generate(arr, cur, result)
        arr.insert(i, cur.pop())
    return result

print(get_permutations([1,2,3]))