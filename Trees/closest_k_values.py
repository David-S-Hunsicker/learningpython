import heapq


def find_k_closest_values(root, target, k):
    heap = []

    def tree_traversal(root):
        if not root:
            return

        tree_traversal(root.left)
        if len(heap) < k:
            heapq.heappush(heap, root.value)
        else:
            if abs(target - root.value) < abs(target - heap[0]):
                heapq.heapreplace(heap, root.value)
            else:
                return
        tree_traversal(root.right)

    tree_traversal(root)
    return heap
