def count_triplets(target, numbers:[]):
    trips = 0;
    numbers.sort()
    end = len(numbers)-1

    for i in range(end):
       lo = i + 1
       hi = end
       while lo < hi:
           if numbers[i] + numbers[lo] + numbers[hi] < target:
               trips += hi-lo
               lo += 1
           else:
               hi -= 1
    return trips

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
print(count_triplets(target, a))