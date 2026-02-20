import copy

N = 3

row_moves = [0, 0, -1, 1]
col_moves = [-1, 1, 0, 0]

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]


class P8Board:
    def __init__(self, board, x, y, depth=0, parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth
        self.parent = parent


# Check valid position
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


# Check goal state
def is_goal(board):
    return board == goal


# Manhattan Distance Heuristic
def heuristic(board):
    h = 0
    for i in range(N):
        for j in range(N):
            val = board[i][j]
            if val != 0:
                gx = (val - 1) // N
                gy = (val - 1) % N
                h += abs(i - gx) + abs(j - gy)
    return h


# Print solution path
def print_solution(node):
    path = []

    while node:
        path.append(node)
        node = node.parent

    path.reverse()

    for i, step in enumerate(path):
        print(f"--- Step {i} ---")
        for row in step.board:
            print(row)
        print()

    print("Goal reached!")


# Hill Climbing Algorithm
def hill_climbing(start_board, x, y):
    current = P8Board(start_board, x, y)
    current_h = heuristic(current.board)

    while True:
        if is_goal(current.board):
            print_solution(current)
            return

        neighbors = []

        # Generate neighbors
        for i in range(4):
            new_x = current.x + row_moves[i]
            new_y = current.y + col_moves[i]

            if is_valid(new_x, new_y):
                new_board = copy.deepcopy(current.board)

                # Swap blank
                new_board[current.x][current.y], new_board[new_x][new_y] = \
                    new_board[new_x][new_y], new_board[current.x][current.y]

                h = heuristic(new_board)
                neighbors.append((h, new_board, new_x, new_y))

        if not neighbors:
            print("No possible moves.")
            return

        # Choose best neighbor (lowest heuristic)
        best = min(neighbors, key=lambda x: x[0])

        if best[0] >= current_h:
            print("Stuck at local minimum or plateau!")
            return

        current = P8Board(best[1], best[2], best[3],
                          current.depth + 1, current)
        current_h = best[0]


# Main
if __name__ == "__main__":
    start = [[1, 2, 3],
             [4, 0, 5],
             [7, 8, 6]]

    x, y = 1, 1

    hill_climbing(start, x, y)
