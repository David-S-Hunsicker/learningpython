"""
iterate through each list and add the value as a key to a sorted dictionary
    OR increment that value if it already exists

loop through the dictionary keys and add all values to a list.
quick sort that list for n(log(n)) time
loop through the sorted keys and add o nodes for each key n where o is the occurences of that key
each k i number of times where i is the frequency of that key's value
Time: O(n log(n))
Space: O(n)
"""

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_k_lists(lists):
    head = LinkedListNode()
    node = head

    key_count = dict()
    # load up our counts dictionary
    for i in range(len(lists)):
        while lists[i] is not None:
            val = lists[i].value
            if val not in key_count:
                key_count[val] = 0
            key_count[val] += 1
            lists[i] = lists[i].next

    # n' = n with duplicates removed
    # insertions will be O(1) instead of O(log(n)) and sorting is O(n' log(n'))
    # sorting a dictionary of n' keys could be less than using a sorted dictionary

    # sort the dictionary by keys
    key_count = sorted(key_count.items(), key=lambda x: x[0])
    # build the resulting linked list
    for key, value in key_count:
        for i in range(value):
            node.next = LinkedListNode(key)
            node = node.next

    return head.next