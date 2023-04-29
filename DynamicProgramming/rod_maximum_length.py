def get_maximum_profit(price):
    price.insert(0, 0) # n time
    for i in range(1, len(price)): # calculate best price for length
        largest = price[i]
        for j in range(i):
            largest = max(largest, price[j] + price[i-j])
        price[i] = largest
    return price[-1]

def get_maximum_profit_include_exclude(price):
    price.insert(0, 0) # n time
    for i in range(1, len(price)): # calculate best price for length
        exclude = price[i] # I don't cut the rope
        include = 0 # I will cut the rope into n pieces
        for j in range(i):
            include = max(include, price[j] + price[i-j])
        price[i] = max(include, exclude)
    return price[-1]

def get_maximum_profit_implicit(price):
    price.insert(0, 0) # n time
    for i in range(1, len(price)): # calculate best price for length
        for j in range(i):
            price[i] = max(price[i], price[j] + price[i-j])
    return price[-1]

def get_maximum_implicit_no_mutation(price):
    memo  = [0]
    memo += price # n time
    for i in range(1, len(memo)): # calculate best price for length
        for j in range(i):
            memo[i] = max(memo[i], memo[j] + memo[i-j])
    return memo[-1]
# Time O(n^2)
# Space: O(1)

price = [1,5,8,9]
print("Not using include/exclude " + str(get_maximum_profit(price)))
price = [1,5,8,9]
print("Using include and exclude " + str(get_maximum_profit_include_exclude(price)))
price = [1,5,8,9]
print("Using include/exclude implicitly " + str(get_maximum_profit_implicit(price)))
price = [1,5,8,9]
print("Using same logic but no mutation " + str(get_maximum_implicit_no_mutation(price)))