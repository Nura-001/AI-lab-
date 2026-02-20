import copy
import heapq

N = 3

row_moves = [0, 0, -1, 1]
col_moves = [-1, 1, 0, 0]

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]


class P8Board:
    def __init__(self, board, x, y, g=0, parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.g = g          # Cost from start
        self.parent = parent


# Check valid move
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


# Check goal state
def is_goal(board):
    return board == goal


# Manhattan Distance Heuristic
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


# Print solution path
def print_solution(node):
    path = []

    while node:
        path.append(node)
        node = node.parent

    path.reverse()

    print("\nSolution Steps:\n")
    for i, step in enumerate(path):
        print(f"--- Step {i} ---")
        for row in step.board:
            print(row)
        print()


# A* Algorithm
def a_star_solve(start_board, x, y):
    visited = set()
    heap = []
    counter = 0   # tie-breaker for heap

    start_h = manhattan_distance(start_board)

    heapq.heappush(heap,
                   (start_h, counter,
                    P8Board(start_board, x, y, 0)))

    while heap:
        f, _, current = heapq.heappop(heap)

        board_tuple = tuple(map(tuple, current.board))

        if board_tuple in visited:
            continue

        visited.add(board_tuple)

        if is_goal(current.board):
            print("Solution found (A* Search)!")
            print_solution(current)
            print("Total moves:", current.g)
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

                board_tuple = tuple(map(tuple, new_board))

                if board_tuple not in visited:
                    counter += 1
                    new_g = current.g + 1
                    h = manhattan_distance(new_board)
                    f_new = new_g + h

                    heapq.heappush(heap,
                                   (f_new, counter,
                                    P8Board(new_board, new_x, new_y,
                                            new_g, current)))

    print("No solution found.")


# Main
if __name__ == "__main__":
    start = [[1, 2, 3],
             [4, 0, 5],
             [7, 8, 6]]

    x, y = 1, 1  # blank position

    a_star_solve(start, x, y)
