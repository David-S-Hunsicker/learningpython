def get_nary_strings(n):
    return nary_string(n, "", [])


def nary_string(n, cur, result):
    if len(cur) == n:
        result.append(cur)
        return
    for i in range(0, n):
        nary_string(n, cur + str(i+1), result)
    return result


print(get_nary_strings(3))
