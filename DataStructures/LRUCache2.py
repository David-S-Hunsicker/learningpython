class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = {}  # Key, Node
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.nodes:
            node = self.nodes[key]
            self._top_(node)
            return node.value
        return -1

    # Inserts node at the top of the cache.
    # If the node exists in cache already updates its position.
    # If the node is new will evict the last node.
    def put(self, key, value):
        # Update
        if key in self.nodes:
            node = self.nodes[key]
        # Create
        else:
            self.capacity += 1
            node = Node(key, value)
            self.nodes[key] = node
            self._remove_(self.tail.prev)

        node.value = value
        self._top_(node)

    # Moves a node to the top of the cache
    def _top_(self, node):
        self._break_links_(node)

        # Insert
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node

    def _remove_(self, node):
        self._break_links_(node)
        del self.nodes[node.key]
        self.capacity -= 1

    # Safely removes a node from the linked list.
    def break_links(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
