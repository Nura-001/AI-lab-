import copy
import heapq

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


# Check valid move
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


# Check goal state
def is_goal(board):
    return board == goal


# Manhattan distance heuristic
def manhattan_distance(board):
    dist = 0
    for i in range(N):
        for j in range(N):
            val = board[i][j]
            if val != 0:
                goal_x = (val - 1) // N
                goal_y = (val - 1) % N
                dist += abs(i - goal_x) + abs(j - goal_y)
    return dist


# Best-First Search (Greedy)
def best_first_solve(start_board, x, y):
    visited = set()
    heap = []
    counter = 0

    start_h = manhattan_distance(start_board)

    heapq.heappush(heap, (start_h, counter,
                          P8Board(start_board, x, y, 0)))

    while heap:
        h, _, current = heapq.heappop(heap)

        board_tuple = tuple(map(tuple, current.board))

        if board_tuple in visited:
            continue

        visited.add(board_tuple)

        if is_goal(current.board):
            print("Solution found (Best-First Search)!")
            print_solution(current)
            return

        # Explore neighbors
        for i in range(4):
            new_x = current.x + row_moves[i]
            new_y = current.y + col_moves[i]

            if is_valid(new_x, new_y):
                new_board = copy.deepcopy(current.board)

                # Swap blank
                new_board[current.x][current.y], new_board[new_x][new_y] = \
                    new_board[new_x][new_y], new_board[current.x][current.y]

                board_t = tuple(map(tuple, new_board))

                if board_t not in visited:
                    counter += 1
                    h_new = manhattan_distance(new_board)

                    heapq.heappush(heap,
                                   (h_new, counter,
                                    P8Board(new_board, new_x, new_y,
                                            current.depth + 1, current)))

    print("No solution found.")


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


if __name__ == "__main__":
    start = [[1, 2, 3],
             [4, 0, 5],
             [7, 8, 6]]

    x, y = 1, 1

    best_first_solve(start, x, y)
