
def find_order(words):
    graph = {}

    chars = set("".join(words))

    # Create a dictionary with all characters as keys and empty lists as values
    for char in chars:
        graph[char] = []

    # Loop through all adjacent words and add edges to the graph
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        min_len = min(len(word1), len(word2))
        for letter in range(min_len):
            if word1[letter] != word2[letter]:
                graph[word1[letter]].append(word2[letter])
                break

    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        for adj in graph[node]:
            if adj not in visited:
                dfs(adj)
        order.append(node)

    # Call DFS on all unvisited nodes
    for node in graph:
        if node not in visited:
            dfs(node)

    # Reverse the result array to get the correct order
    order.reverse()

    # Convert the result array to a string and return
    return "".join(order) if len(order) == len(chars) else ""

words= ["baa", "abcd", "abca", "cab", "cad"]
print(find_order(words))
words = ["wrt","wrf","er","ett","rftt"]
print(find_order(words))

#
# def find_order(words):
#     r = []
#     adj_map = {}
#     visited = set()
#     def top_sort(node):
#         visited.add(node)
#         for neighbor in adj_map[node]:
#             if neighbor not in visited:
#                 top_sort(neighbor)
#         r.append(node)
#
#     def build_adj():
#         adj_map[words[0][0]] = set() # there's always one letter.
#         # compare the first non-matching characters and add them
#         for i in range(len(words)-1):
#             for j in range(min(len(words[i]), len(words[i+1]))):
#                 if words[i][j] != words[i+1][j]: # first non-match implies order
#                     if words[i][j] not in adj_map:
#                         adj_map[words[i][j]] = set()
#                     if words[i+1][j] not in adj_map:
#                         adj_map[words[i+1][j]] = set()
#                     adj_map[words[i][j]].add(words[i+1][j])
#                     break
#     build_adj()
#     for key, val in adj_map.items():
#         if key not in visited:
#             top_sort(key)
#     r.reverse()
#     return "".join(r)
