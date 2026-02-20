import copy
from collections import deque

N = 3

row_moves = [0, 0, -1, 1]
col_moves = [-1, 1, 0, 0]

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]


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
    return board == goal


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


def bfs_solve(start_board, x, y):
    queue = deque([P8Board(start_board, x, y, 0)])
    visited = set()
    visited.add(tuple(map(tuple, start_board)))

    while queue:
        current = queue.popleft()   # FIFO → BFS

        if is_goal(current.board):
            print("Solution found (BFS)!")
            print_solution(current)
            return

        for i in range(4):
            new_x = current.x + row_moves[i]
            new_y = current.y + col_moves[i]

            if is_valid(new_x, new_y):
                new_board = copy.deepcopy(current.board)

                # swap blank
                new_board[current.x][current.y], new_board[new_x][new_y] = \
                    new_board[new_x][new_y], new_board[current.x][current.y]

                board_tuple = tuple(map(tuple, new_board))

                if board_tuple not in visited:
                    visited.add(board_tuple)
                    queue.append(
                        P8Board(new_board, new_x, new_y,
                                current.depth + 1, current)
                    )

    print("No solution found.")


if __name__ == "__main__":
    start = [[1, 2, 3],
             [4, 0, 5],
             [7, 8, 6]]

    x, y = 1, 1  # position of blank (0)

    bfs_solve(start, x, y)
