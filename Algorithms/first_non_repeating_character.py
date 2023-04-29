class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def first_non_repeating_character(s):
    d = {}
    seen = set()
    head = Node(0)
    tail = Node(0)
    head.next = tail
    tail.prev = head
    for c in s:
        if not c.isalpha(): # assuming white space doesn't count
            continue
        if c not in seen:
            n = Node(c)
            tail.prev.next = n
            n.prev = tail.prev
            n.next = tail
            tail.prev = n
            d[c] = n
            seen.add(c)
        else:
            if c in d:
                d[c].prev.next = d[c].next
                d[c].next.prev = d[c].prev
                del d[c]
    return head.next.val


s = "the faint red box shelters a fox that dances in the woods at night under the bright starry lights."
# s = "abbca"
print(first_non_repeating_character(s))