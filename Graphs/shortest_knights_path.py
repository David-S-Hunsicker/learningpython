import queue
# using a 1d array to represent a 2d board is not worth the optimization in an interview
def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    visited = [False] * (rows * cols)

    def position(row, col):
        return row * cols + col

    end_pos = position(end_row, end_col)

    def next_positions(pos):
        positions = []
        r = pos[0] % cols
        if  r < cols - 1:
            positions.append(pos[0] - 2 * cols + 1)
            positions.append(pos[0] + 2 * cols + 1)
        if r < cols - 2:
            positions.append(pos[0] + 1 * cols + 2)
            positions.append(pos[0] - 1 * cols + 2)
        if r >= 1:
            positions.append(pos[0] + 2 * cols - 1)
            positions.append(pos[0] - 2 * cols - 1)
        if r >= 2:
            positions.append(pos[0] + 1 * cols - 2)
            positions.append(pos[0] - 1 * cols - 2)
        return positions

    def valid(pos):
        return pos >= 0 and pos <= rows * cols - 1

    def bfs(pos):
        q = queue.Queue()
        q.put((pos, 0))
        visited[pos] = True
        while not q.empty():
            level = q.qsize()
            for i in range(level):
                pos = q.get()
                # board[pos] = distance
                if pos[0] == end_pos:
                    return pos[1]
                # put all the next moves inside the queue
                for next_position in next_positions(pos):
                    if valid(next_position) and not visited[next_position]:
                        visited[next_position] = True
                        q.put((next_position, 1 + pos[1]))
        return -1

    return bfs(position(start_row, start_col))