
def find_combinations(n, k):
    result = []
    current = []
    combos(1, n, k, current, result)
    return result

def combos(current_num, n, k, current, result):
    if len(current) == k:
        result.append(list(current))
        return
    if current_num == n + 1:
        return

    # recursing before appending is depth first ( high numbers will appear first )
    # recursing after appending + popping gives breadth ( lower combos will appear first)
    current.append(current_num)
    combos(current_num + 1, n, k, current, result)
    current.pop()
    combos(current_num + 1, n, k, current, result)

print(find_combinations(5, 2))