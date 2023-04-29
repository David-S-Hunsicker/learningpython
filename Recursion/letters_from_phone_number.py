def get_words_from_phone_number(phone_number):
    letters_for_number = {
        '2': ["a", "b", "c"],
        '3': ["d", "e", "f"],
        '4': ["g", "h", "i"],
        '5': ["j", "k", "l"],
        '6': ["m", "n", "o"],
        '7': ["p", "q", "r", "s"],
        '8': ["t", "u", "v"],
        '9': ["w", "x", "y", "z"],
    }

    def helper(results, iteration, partial):
        if iteration == 7:
            results.append("".join(partial))
            return

        num = phone_number[iteration]
        if num == '1' or num == '0':  # don't add or access dictionary
            helper(results, iteration + 1, partial)
        else:
            for letter in letters_for_number[num]:
                partial.append(letter)
                helper(results, iteration + 1, partial)
                partial.pop()

    results = []
    helper(results, 0, [])
    return results if len(results) > 0 else [""]


number = '1234567'
print(get_words_from_phone_number(number))

number = '1010101'
print(get_words_from_phone_number(number))
