# r result              Recursion
# i iteration           Is
# s set                 Stupid
# p partial-solution    Powerful


def helper(r, i, s, p):

    if i == len(s):
        r.append(list(p))
        return

    # exclude
    helper(r, i+1, s, p)
    # include
    p.append(s[i])
    helper(r, i+1, s, p)
    p.pop()

def generate_subsets(s):
    r = []
    helper(r, 0, s, [])
    return r

print(generate_subsets([1,2,3]))
