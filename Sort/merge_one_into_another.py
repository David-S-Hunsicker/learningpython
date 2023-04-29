def merge_one_into_another(first:list, second:list):
    if len(first) > len(second):
        longer = first
        short = second
    else:
        longer = second
        shorter = first

    s = len(shorter) - 1
    l = len(longer) - 1 - len(shorter)
    i = len(longer) - 1
    while s >= 0 and l >= 0:
        if longer[l] >= shorter[s]:
            longer[i] = longer[l]
            l -= 1
        else:
            longer[i] = shorter[s]
            s -= 1
        i -= 1

    while s >= 0:
        longer[i] = shorter[s]
        s -= 1
        i-= 1
    while l >= 0:
        longer[i] = longer[l]
        l -= 1
        i -= 1
    return longer


first = [34, 44, 62, 113, 141, 168, 198]
second=[9, 18, 88, 88, 127, 178, 199, 0, 0, 0, 0, 0, 0, 0]
print(merge_one_into_another(first, second))
