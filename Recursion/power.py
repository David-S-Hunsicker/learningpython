def calculate_power(base, power):
    if power == 1: return base
    if power == 0: return 1
    half_power = power // 2
    root_base = calculate_power(base, half_power)
    if power % 2 == 0: return (root_base * root_base) % 1000000007
    else: return (base * root_base * root_base) % 1000000007



a = 2
b = 4
print(calculate_power(a, b))
