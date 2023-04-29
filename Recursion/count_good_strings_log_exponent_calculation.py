MOD = (10 ** 9 + 7)


def count_good_digit_strings(n):
    def log_exp(power, base):
        if power == 0: return 1
        if power == 1: return base

        half_power = power // 2  # cut the exponent in half
        root_base = log_exp(half_power, base) % MOD
        if power % 2 == 1:
            return (base * root_base * root_base) % MOD
        else:
            return (root_base * root_base) % MOD

    # odds are prime 4^n
    # evens are even 5^n
    odds = n // 2
    evens = odds + n % 2

    return (log_exp(evens, 5) * log_exp(odds, 4)) % (10 ** 9 + 7)