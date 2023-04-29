from collections import deque

# this is a bfs implementation that stops when we find any solution since only shortest paths matter.
def get_all_shortest_transformation_sequences(start_word, target_word, words):
    adj_map = {}  # word -> set of adjacent words
    words.append(start_word)

    def is_adjacent(word, word2):
        count = 0
        for i in range(len(word)):
            if word[i] != word2[i]:
                count += 1
            if count > 1: return False
        return count == 1

    def build_adjacencies():
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                word = words[i]
                word2 = words[j]
                if is_adjacent(word, word2):
                    if word not in adj_map:
                        adj_map[word] = set()
                    if word2 not in adj_map:
                        adj_map[word2] = set()
                    adj_map[word].add(word2)
                    adj_map[word2].add(word)

    def bfs(start_word):
        q = deque()
        solution = False # as soon as we find a shortest path, stop processing levels.
        q.append((start_word, [start_word]))
        while q and not solution:
            size = len(q)
            for i in range(size):
                word, path = q.popleft()
                for adj in adj_map[word]:
                    if adj in path:
                        continue
                    new_path = path[:]
                    new_path.append(adj)
                    if adj == target_word:
                        solution = True
                        results.append(new_path)
                    else:
                        q.append((adj, new_path))
    results = []
    build_adjacencies()
    bfs(start_word)
    return results
start_word = "hot"
target_word = "dog"
words = ["cat", "dog", "hat", "dot", "cot", "hog"]
print(get_all_shortest_transformation_sequences(start_word, target_word, words))