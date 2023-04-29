# s: original string,
# i: index to be worked on
# slate: partial solution
# results: accumulating solution
def helper(s, i, slate, results):
    # base
    if i == len(s):
        results.append("".join(slate))
        return

    # recursive
    if s[i].isdigit():
        slate.append(s[i])
        helper(s, i + 1, slate, results)
        slate.pop()
    else:
        slate.append(s[i].lower())
        helper(s, i + 1, slate, results)
        slate.pop()
        slate.append(s[i].upper())
        helper(s, i + 1, slate, results)
        slate.pop()


def letter_case_permutation(s):
    r = []
    helper(s, 0, [], r)
    return r


print(letter_case_permutation("abcd"))
# Time: o n, O(2^n * n)
# Space: n