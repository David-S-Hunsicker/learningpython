import random


def sort_array(arr):
    chars = {}
    for i in range(len(arr)):
        char = arr[i]
        if char not in chars: chars[char] = 0
        chars[char] += 1
    chars = sorted(chars.items())
    results = []
    for key, val in chars:
        for _ in range(val):
            results.append(key)
    return results


arr = ["a", "s", "d", "f", "g", "*", "&", "!", "z", "y", "a", "a"]

print(sort_array(arr))
