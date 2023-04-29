# given a set of distinct integer values, return all possible permutations
# Time: N^2
# Space: N^2

def permute(nums):
    r = []

    def helper(i, s, p):
        # base
        if i == len(s):
            r.append(p[:])
            return

        # recursion
        for j in range(i, (len(s))):
            #it's okay for an index to swap with itself,
            # because that's the choice of not swapping the order
            # and is a valid permutation
            s[i], s[j] = s[j], s[i]
            p.append(s[i])
            helper(i+1, s, p)
            p.pop()
            s[i], s[j] = s[j], s[i]
    helper(0, nums, [])
    return r
print(permute([1,2,3]))