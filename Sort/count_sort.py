import random


def count_sort(a:[], num_range:int):

    counts = [0] * (2*num_range+1)
    for i in range(len(a)):
        counts[a[i]+num_range]+=1
    index = 0;
    for i in range(len(counts)):
        while counts[i] > 0:
            a[index] = i-num_range
            index += 1
            counts[i]-=1


l = [0] * 25
num_range = 10
for i in range(len(l)):
    l[i] = random.randrange(num_range*-1, num_range+1)
print("input ",  l)
count_sort(l, num_range)
print("output ", l)