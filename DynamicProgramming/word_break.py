# Recursive
def word_break(s, words_dictionary):
    words_dictionary = set(words_dictionary)

    def helper(s):
        if len(s) == 0:
            return True
        for i in range(len(s)):
            if s[:i + 1] in words_dictionary:
                if helper(s[i + 1:]):
                    return True

    return True if helper(s) else False
# DP
def word_breaks(s, words_dictionary):




s = "kickstartkick"
d = ["kick", "kickstart", "startkick"]

print(word_break(s, d))
