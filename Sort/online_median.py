from heapq import *
def online_median(stream):
    max_q = [] # smaller numbers
    min_q = [] # large numbers, flip the sign to get desired behavior
    results = []
    for num in stream: # we want to make sure everything lands on max_q
        if len(max_q) == len(min_q):
            heappush(min_q, -heappushpop(max_q, -num))
            results.append(min_q[0])
        else:
            heappush(max_q, -heappushpop(min_q, num))
            # results.append((min_q[0]-max_q[0])//2)
            results.append((max_q[0]* -1 + min_q[0] )//2)
    return results

# 1 1 2 2 3
stream = [1, 2, 3, 4, 5]
print(online_median(stream))
