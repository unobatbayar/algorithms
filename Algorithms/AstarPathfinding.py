import heapq

# Function to calculate the Manhattan distance between two points
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# A* search algorithm
def astar_search(graph, start, goal):
    # Initialize the open and closed sets
    open_set = []
    closed_set = set()

    # Create a dictionary to keep track of the cost to reach each node
    # Initialize all nodes with a cost of infinity except the start node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # Create a dictionary to keep track of the estimated total cost for each node
    f_score = {node: float('inf') for node in graph}
    f_score[start] = manhattan_distance(start, goal)

    # Add the start node to the open set with its estimated cost
    heapq.heappush(open_set, (f_score[start], start))

    while open_set:
        # Pop the node with the lowest estimated cost from the open set
        current = heapq.heappop(open_set)[1]

        if current == goal:
            # Goal reached, return the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        # Add the current node to the closed set
        closed_set.add(current)

        for neighbor in graph[current]:
            if neighbor in closed_set:
                # Skip if the neighbor is already evaluated
                continue

            # Calculate the tentative cost to reach the neighbor
            tentative_g_score = g_score[current] + manhattan_distance(current, neighbor)

            if tentative_g_score < g_score[neighbor]:
                # This path is better than any previous one, update the scores
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + manhattan_distance(neighbor, goal)

                if neighbor not in open_set:
                    # Add the neighbor to the open set if it's not already there
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    # Open set is empty and goal was not reached, return an empty path
    return []

# Example usage

# Define the graph as an adjacency dictionary
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A', 'D', 'E'},
    'D': {'B', 'C', 'F'},
    'E': {'C', 'F', 'G'},
    'F': {'D', 'E', 'G'},
    'G': {'E', 'F'}
}

start_node = 'A'
goal_node = 'G'

# Find the shortest path using A* search
path = astar_search(graph, start_node, goal_node)

print("Shortest path:", path)
