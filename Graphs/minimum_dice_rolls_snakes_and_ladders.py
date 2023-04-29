def minimum_number_of_rolls(n, moves):
    queue = [0]
    visited = [False] * n
    result = 0
    while queue:
        new_queue = []
        for cell in queue:
            if cell == n - 1:
                return result
            for move in range(cell + 1, cell + 7):
                if move < n and not visited[move]:
                    visited[move] = True
                    if moves[move] != -1:
                        visited[moves[move]] = True
                        new_queue.append(moves[move])
                    else:
                        new_queue.append(move)
        result += 1
        queue = new_queue
    return -1
n = 8
moves = [-1, -1, -1, -1, -1, -1, -1, -1]
print(minimum_number_of_rolls(n, moves))