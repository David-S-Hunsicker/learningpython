
def well_formed(p, k):
    v = 0
    for i in range(len(p)):
        if p[i] == "(":
            v += 1
        else:
            if v == 0:
                return False
            else:
                v -= 1
    return len(p) == k and v == 0


def helper(r, i, p, k):
    if i > k * 2:
        return

    if i == (k * 2) and well_formed(p, k * 2):
        r.add("".join(p))
        return

    # left
    p.append("(")
    helper(r, i + 1, p, k)
    p.pop()
    # right
    p.append(")")
    helper(r, i + 1, p, k)
    p.pop()


def find_all_well_formed_brackets(n):
    r = set()
    helper(r, 0, [], n)
    return list(r)

print(find_all_well_formed_brackets(3))