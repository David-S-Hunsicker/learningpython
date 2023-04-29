class max_heap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return item

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)

    def _bubble_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._bubble_down(largest)

heap = max_heap()
heap.push(5)
heap.push(7)
heap.push(3)
heap.push(12)
heap.push(1)

print(heap.pop()) # 12
print(heap.pop()) # 7
print(heap.pop()) # 5
