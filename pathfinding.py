import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(node, rows, cols):
    x, y = node
    neighbors = []
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbors.append((nx, ny))
    return neighbors


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


def dijkstra_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        current_cost, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current, rows, cols):
            if grid[neighbor[0]][neighbor[1]] == 0: # impassable
                continue

            tentative_g = g_score[current] + grid[neighbor[0]][neighbor[1]]

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                heapq.heappush(open_set, (tentative_g, neighbor))

    return None



def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    open_heap = []
    heapq.heappush(open_heap, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    open_set = {start}
    closed_set = set()

    while open_heap:
        _, current = heapq.heappop(open_heap)

        if current == goal:
            return reconstruct_path(came_from, current)
        
        open_set.discard(current)
        closed_set.add(current)

        for neighbor in get_neighbors(current, rows, cols):
            # impassable terrain
            if grid[neighbor[0]][neighbor[1]] == 0:
                continue

            if neighbor in closed_set:
                continue
            
            tentative_g = g_score[current] + grid[neighbor[0]][neighbor[1]]

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                if neighbor not in open_set:
                    heapq.heappush(open_heap, (f_score[neighbor], neighbor))
                    open_set.add(neighbor)

    return None # no path found



def update_grid(grid, obstacle_positions):
    for (x, y) in obstacle_positions:
        grid[x][y] = 0 # mark as impassable



if __name__ == "__main__":
    grid = [
         [1, 1, 1, 1],
        [1, 5, 0, 1],
        [1, 1, 2, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1]
     ]

    start = (0, 0)
    goal = (4, 3)

    print("Dijkstra path:", dijkstra_search(grid, start, goal))
    print("A* path:", a_star_search(grid, start, goal))

    update_grid(grid, [(2, 2), (3, 2)])
    print("Grid updated with dynamic obstacles.")
    print("New A* path:", a_star_search(grid, start, goal))