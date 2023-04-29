def get_binary_strings(n):
    return binary_string(n, "", [])


def binary_string(n, cur, result):
    if n == 0:
        result.append(cur)
        return

    binary_string(n - 1, cur + "0", result)
    binary_string(n - 1, cur + "1", result)
    return result


print(get_binary_strings(4))
