def get_distinct_subsets(s):
    def helper(results, iteration, p):
        if iteration == len(s):
            results.add("".join(p))
            return

        # exclude
        helper(results, iteration + 1, p)
        # include
        p.append(s[iteration])
        helper(results, iteration + 1, p)
        p.pop()  # maybe don't need this

    s = ''.join(sorted(s))
    results = set()
    helper(results, 0, [""])
    results = list(results)
    return results


s = "dc"
print(get_distinct_subsets(s))

print(''.join(sorted(s)))

# The question calls for the subsets to be sorted so we sorted the input before processing.