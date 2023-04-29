def generate_palindromic_decompositions(s):
    results = []

    def is_palindrome(start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def helper(start, end, partial):

        if end == len(s) - 1:
            partial.append(s[end])
            if is_palindrome(start, end):
                results.append("".join(partial))
            partial.pop()
            return

        partial.append(s[end])

        if is_palindrome(start, end):
            if end < len(s) - 1:
                partial.append("|")
                helper(end + 1, end + 1, partial)
                partial.pop()
            else:
                helper(end + 1, end + 1, partial)

        helper(start, end + 1, partial)
        partial.pop()

    helper(0, 0, [])
    return results


s = "abracadabra"
print(generate_palindromic_decompositions(s))
