import queue


def string_transformation(words, start, stop):
    def valid_transform(first, second):
        different = 0;
        for i in range(len(first)):
            if first[i] != second[i]:
                different += 1
                if different > 1:
                    return False
        return different == 1

    def build_result():
        word = stop
        while True:
            result.append(word)
            word = parent[word]
            if word == start:
                result.append(start)
                break

    def bfs(result, word):
        q = queue.Queue()
        visited.add(word)
        q.put(word)
        while not q.empty():
            word = q.get()
            if valid_transform(word, stop):
                parent[stop] = word
                build_result()
                return True
            for transform in adj_map[word]:
                if transform not in visited:
                    parent[transform] = word
                    visited.add(transform)
                    q.put(transform)
        return False

    if len(words) == 0 and not valid_transform(start, stop):
        return ["-1"]

    words = set(words)  # remove duplicates
    words.add(start)
    adj_map = {}
    visited = set()
    parent = {}
    result = []
    keys = []
    keys += words

    def build_adj_simple():
        # build the adjacency map
        for key in keys:
            for word in words:
                if valid_transform(key, word):
                    if key not in adj_map:
                        adj_map[key] = set()
                    adj_map[key].add(word)

    def build_adj_complex():
        for key in keys:
            for i in range(len(key)):
                new_key = list(key)
                orig = new_key[i]
                c = ord('a')
                while c <= ord('z'):
                    if chr(c) != orig:
                        new_key[i] = chr(c)
                        if "".join(new_key) in words:
                            if key not in adj_map:
                                adj_map[key] = set()
                            adj_map[key].add("".join(new_key))
                    c += 1

    if len(words) > 10:
        build_adj_complex()
    else:
        build_adj_simple()

    if bfs(result, start):
        result.reverse()
        return result
    return ["-1"]


words = ["cccw", "accc", "accw"]
start = "cccc"
stop = "cccc"
print(string_transformation(words, start, stop))
