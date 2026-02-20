import heapq 
# Goal state 
GOAL = ((1, 2, 3), 
(4, 5, 6), 
(7, 8, 0)) 
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right 
# Manhattan distance heuristic 
def heuristic(state): 
dist = 0 
for i in range(3): 
for j in range(3): 
val = state[i][j] 
if val != 0: 
x, y = divmod(val - 1, 3) 
dist += abs(x - i) + abs(y - j) 
return dist 
# Find blank (0) position 
def find_blank(state): 
for i in range(3): 
for j in range(3): 
if state[i][j] == 0: 
return i, j 
# Generate all child states 
def generate_children(state): 
children = [] 
x, y = find_blank(state) 
for dx, dy in MOVES: 
nx, ny = x + dx, y + dy 
if 0 <= nx < 3 and 0 <= ny < 3: 
new_state = [list(row) for row in state] 
new_state[x][y], new_state[nx][ny] = new_state[nx][ny], 
new_state[x][y] 
children.append(tuple(tuple(row) for row in new_state)) 
return children 
# AO* Algorithm 
def ao_star(start): 
open_list = [] 
heapq.heappush(open_list, (heuristic(start), 0, start, [start])) 
visited = set() 
while open_list: 
f, g, state, path = heapq.heappop(open_list) 
if state == GOAL: 
return path 
if state in visited: 
continue 
visited.add(state) 
for child in generate_children(state): 
if child not in visited: 
new_g = g + 1 
new_f = new_g + heuristic(child) 
heapq.heappush(open_list, (new_f, new_g, child, path + 
[child])) 
return None 
# Print solution 
def print_solution(path): 
for i, step in enumerate(path): 
print(f"--- Step {i} ---") 
for row in step: 
print(row) 
print() 
if __name__ == "__main__": 
start_state = ((1, 2, 3), 
(4, 0, 6), 
(7, 5, 8)) 
solution = ao_star(start_state) 
if solution: 
print("Solution found (AO* Search)!") 
print_solution(solution) 
else: 
print("No solution found")
