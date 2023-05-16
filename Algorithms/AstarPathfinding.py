import heapq

# Function to calculate the Manhattan distance between two points (coordinates)
def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

# A* search algorithm
def astar_search(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Goal reached, reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor in get_neighbors(current, grid):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current

    # Open set is empty and goal was not reached, return an empty path
    return []

# Function to get valid neighbors of a grid cell
def get_neighbors(cell, grid):
    row, col = cell
    rows = len(grid)
    cols = len(grid[0])
    neighbors = []
    if row > 0 and grid[row - 1][col] != '#':
        neighbors.append((row - 1, col))
    if row < rows - 1 and grid[row + 1][col] != '#':
        neighbors.append((row + 1, col))
    if col > 0 and grid[row][col - 1] != '#':
        neighbors.append((row, col - 1))
    if col < cols - 1 and grid[row][col + 1] != '#':
        neighbors.append((row, col + 1))
    return neighbors

# Example usage

# Define the grid as a 2D list
grid = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '#', '.'],
    ['.', '.', '#', '#', '.', '#', '.'],
    ['.', '.', '#', '#', '.', '#', '.'],
    ['.', '.', '#', '#', '.', '#', '.'],
    ['.', '.', '#', '#', '.', '#', '.'],
    ['.', '.', '#', '#', '.', '#', '.'],
    ['#', '.', '#', '.', '.', '#', 'G']
]

start = (0, 0)
goal = (9, 6)

# Find the shortest path using A* search
path = astar_search(grid, start, goal)

print("Shortest path:", path)
