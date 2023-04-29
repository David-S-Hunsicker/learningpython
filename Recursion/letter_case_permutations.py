# RISP
def letter_case_permutations(s):
    def helper(results, iteration, s, partial):
        # complete partial solution
        if iteration == len(s):
            results.append("".join(partial))
            return

        if s[iteration].isalpha():
            upper = s[iteration].upper()
            lower = s[iteration].lower()
            # upper
            partial.append(upper)
            helper(results, iteration + 1, s, partial)
            partial.pop()
            # lower
            partial.append(lower)
            helper(results, iteration + 1, s, partial)
            partial.pop()
        else:
            partial.append(s[iteration])
            helper(results, iteration + 1, s, partial)
            partial.pop()

    results = []
    helper(results, 0, s, [])
    return results