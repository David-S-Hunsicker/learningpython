"""
Asymptotic complexity in terms of the number of queens `n`:
* Time: Exponential, i.e. O(C^n) where C is a constant.
* Auxiliary space: Exponential.
* Total space: Exponential.
"""


def find_all_arrangements(n):
    """
    Any candidate solution or complete solution will have exactly
    one queen in each row, so we can store the entire solution in
    a one-dimensional vector of integers. For example, the following grid
    --q-
    q---
    ---q
    -q--
    has queens at positions (1, 2), (1, 0), (2, 3), (3, 1).
    Using a vector, this can be represented as
    candidate[0] = 2,
    candidate[1] = 0,
    candidate[2] = 3,
    candidate[3] = 1

    Initialized as "empty board", candidate instance will be modified
    by the recursive function to try all possible arrangements.
    """
    candidate = [None] * n

    # For collecting valid arrangements; same format as candidates.
    solutions = []

    # All three "occupied" vectors are initially initialized to false since the board is empty:
    # n columns for n rows
    col_occupied = [False] * n
    # for n * n board there are 2*n-1 slash diagonals
    slash_diagonal_occupied = [False] * (2*n-1)
    # ... and 2*n-1 backslash diagonals.
    backslash_diagonal_occupied = [False] * (2*n-1)

    # Returns True if we can place a queen at position (row, col).
    def is_safe(row, col):
        return not (col_occupied[col] or
                    slash_diagonal_occupied[row+col] or
                    backslash_diagonal_occupied[row-col+n-1])

    # Converts solutions from list<int> into list<string>.
    def generate_output(solutions):
        output = []
        for arr in solutions:
            o = [['-'] * len(arr) for _ in range(len(arr))]
            for r, c in enumerate(arr):
                o[r][c] = 'q'
            output.append([''.join(row) for row in o])
        return output

    # The recursive function.
    def find_all_arrangements_util(candidate, row):
        if row == n:
            # make a copy and append to solutions
            solutions.append([x for x in candidate])
            return

        for col in range(0, n):
            if is_safe(row, col):
                candidate[row] = col
                # mark the column and both diagonals as occupied
                col_occupied[col] = True
                slash_diagonal_occupied[row+col] = True
                backslash_diagonal_occupied[row-col+n-1] = True

                # Try to place any more queens (from the next row down).
                find_all_arrangements_util(candidate, row+1)

                # We have explored all the solutions with current value of "candidate";
                # now we need to reset it in order to try the next candidate:
                col_occupied[col] = False
                slash_diagonal_occupied[row+col] = False
                backslash_diagonal_occupied[row-col+n-1] = False

    # Start with an empty board from the 0th row:
    find_all_arrangements_util(candidate, 0)
    return generate_output(solutions)