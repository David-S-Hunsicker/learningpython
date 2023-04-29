
def tower_of_hanoi(n):
    result = []
    helper(n, 1, 2, 3, result)
    return result

def helper(n, s, a, d, result):
    if n == 1: # base case
        result.append(list([s, d]))
        return
    # general case
    # if the stack is >1 then use aux as destination
    helper(n-1, s, d, a, result)
    result.append(list([s,d]))
    helper(n-1, a, s, d, result)

print(tower_of_hanoi(3))