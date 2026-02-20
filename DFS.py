import copy

N = 3

row_moves = [0, 0, -1, 1]
col_moves = [-1, 1, 0, 0]


class P8Board:
    def __init__(self, board, x, y, depth, parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth
        self.parent = parent


def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


def is_goal(board):
    goal = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]
    return board == goal


def print_solution(node):
    path = []
    while node:
        path.append(node.board)
        node = node.parent

    path.reverse()

    print("\nSolution Steps:\n")
    for step in path:
        for row in step:
            print(row)
        print()


def dfs_solve(start_board, x, y):
    stack = []
    visited = set()

    visited.add(tuple(map(tuple, start_board)))
    stack.append(P8Board(start_board, x, y, 0))

    while stack:
        current = stack.pop()

        if is_goal(current.board):
            print("Solution found!")
            print_solution(current)
            return

        for i in range(4):
            new_x = current.x + row_moves[i]
            new_y = current.y + col_moves[i]

            if is_valid(new_x, new_y):
                new_board = copy.deepcopy(current.board)

                # Swap blank (0) with new position
                new_board[current.x][current.y], new_board[new_x][new_y] = \
                    new_board[new_x][new_y], new_board[current.x][current.y]

                board_tuple = tuple(map(tuple, new_board))

                if board_tuple not in visited:
                    visited.add(board_tuple)
                    stack.append(
                        P8Board(new_board, new_x, new_y,
                                current.depth + 1, current)
                    )

    print("No solution found.")


# Example start state
start_board = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

# Find blank position
for i in range(N):
    for j in range(N):
        if start_board[i][j] == 0:
            x, y = i, j

dfs_solve(start_board, x, y)
