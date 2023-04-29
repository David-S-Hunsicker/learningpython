# build a min heap of size k.
# when iterating through the set S of size n, if s[i] is bigger than the peek() of heap,
#    then replace it and bubble it down
# when we want the largest number just check the back number of the heap. it will be the largest.
# insert a number from append_stream and then append the heap.max to the results list
# do this len(append_stream) times
# return results list

def kth_largest(kth_index, initial_stream, append_stream):
    h = heap(kth_index)
    r = []
    # load up the min heap
    for i in range(len(initial_stream)):
        h.insert(initial_stream[i])

    # attempt to load in each item in append
    for i in range(len(append_stream)):
        h.insert(append_stream[i])
        r.append(h.get_smallest())
    return r

class heap:
    def __init__(self, size):
        self.heap = [-2**31] * size
    # the kth largest item is at the beginning of the min heap
    def get_smallest(self):
        return self.heap[0]
    # take a large number and fit it in
    def _bubble_down(self, index):
        l = index * 2 + 1
        r = index * 2 + 2
        smallest = index
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
        if smallest != index:
            self._bubble_down(smallest)
    # only add a number to the min heap if its among the k largest elements
    def insert(self, num):
        if num > self.heap[0]:
            self.heap[0] = num;
            self._bubble_down(0)


k = 2
i_stream = [4,6]
append_stream = [5, 2, 20]
print(kth_largest(k, i_stream, append_stream))
