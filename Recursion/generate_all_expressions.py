def generate_all_expressions(s, target):
    def helper(pos, curr_str, value, prev):
        if pos == n:
            if value == target:
                res.append(curr_str)
            return

        for i in range(pos, n):
            curr = s[pos:i + 1]
            curr_int = int(curr)
            if pos == 0:
                helper(i + 1, curr_str + curr, curr_int, curr_int)
            else:
                helper(i + 1, curr_str + '+' + curr, value + curr_int, curr_int)
                helper(i + 1, curr_str + '*' + curr, (value - prev) + prev * curr_int, prev * curr_int)

    n = len(s)
    res = []
    helper(0, "", 0, 0)
    return res


print(generate_all_expressions("202", 4))
