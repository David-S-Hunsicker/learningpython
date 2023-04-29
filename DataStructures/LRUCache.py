class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = tail
        self.tail.prev = head

    def get(self, key):
        if key in self.nodes:
            node = self.nodes[key]
            self._top_(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._top_(node)
        else:
            node = Node(key, value)
            self.nodes[key] = node
            self._top_(node)
        if len(self.nodes) > self.capacity: self._remove_()

    def _remove_(self):
        node = tail.prev
        tail.prev = node.prev
        node.prev.next = tail
        del self.nodes[node.key]

    def _top_(self, node):
        if node == self.head.next: return

        if node.next: node.prev.next = node.next
        if node.prev: node.next.prev = node.prev

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node