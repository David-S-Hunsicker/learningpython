def generate_all_subsets(s):
    ns = []
    for i in range(len(s)):
        ns.append(s[i])
    result = []
    generate([], ns, result, 0)
    return result


def generate(cur, s, result, i):
    if i == len(s):
        w = ""
        for i in range(len(cur)):
            w += cur[i]
        result.append(w)
        return
    # exclude s[i]
    generate(cur, s, result, i + 1)
    # include s[i] for this level only
    cur += s[i]
    generate(cur, s, result, i + 1)
    # remove s[i] so it doesn't effect other results
    cur.pop()


print(generate_all_subsets("abc"))
