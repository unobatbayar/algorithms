"""
A* (A-Star) Pathfinding Algorithm

A* is an informed search algorithm that finds the shortest path from a start
node to a goal node. It uses a heuristic function to estimate the distance
to the goal, making it more efficient than Dijkstra's for pathfinding.

Time Complexity: O(b^d) where b is branching factor, d is depth
Space Complexity: O(b^d)

The algorithm uses: f(n) = g(n) + h(n)
- g(n): cost from start to node n
- h(n): heuristic estimate from node n to goal
- f(n): estimated total cost through n
"""


import heapq


def a_star(graph, start, goal, heuristic):
    """
    Finds shortest path from start to goal using A* algorithm.
    
    Args:
        graph: Dictionary representing weighted graph {node: [(neighbor, weight), ...]}
        start: Starting node
        goal: Target node
        heuristic: Function that estimates distance from a node to goal
    
    Returns:
        Tuple (distance, path) where path is list of nodes, or (None, None) if no path
    """
    # Priority queue: (f_score, g_score, node, path)
    # f_score = g_score + heuristic
    open_set = [(0, 0, start, [start])]
    
    # Set of nodes already evaluated
    closed_set = set()
    
    # Cost from start to each node
    g_score = {start: 0}
    
    while open_set:
        # Get node with lowest f_score
        current_f, current_g, current, path = heapq.heappop(open_set)
        
        if current in closed_set:
            continue
        
        closed_set.add(current)
        
        # Goal reached
        if current == goal:
            return current_g, path
        
        # Check all neighbors
        for neighbor, weight in graph.get(current, []):
            if neighbor in closed_set:
                continue
            
            # Calculate tentative g_score
            tentative_g = current_g + weight
            
            # If this path to neighbor is better, record it
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor, path + [neighbor]))
    
    return None, None  # No path found


def manhattan_distance(node1, node2):
    """
    Manhattan distance heuristic for grid-based pathfinding.
    Assumes nodes are (x, y) tuples.
    """
    if isinstance(node1, tuple) and isinstance(node2, tuple):
        return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
    return 0


def euclidean_distance(node1, node2):
    """
    Euclidean distance heuristic.
    Assumes nodes are (x, y) tuples.
    """
    if isinstance(node1, tuple) and isinstance(node2, tuple):
        return ((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2) ** 0.5
    return 0


# Example usage
if __name__ == "__main__":
    # Example graph: {node: [(neighbor, weight), ...]}
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
    
    # Simple heuristic: always returns 0 (A* becomes Dijkstra's)
    def zero_heuristic(node, goal):
        return 0
    
    print("A* pathfinding from 'A' to 'E':")
    distance, path = a_star(graph, 'A', 'E', zero_heuristic)
    
    if path:
        print(f"  Distance: {distance}")
        print(f"  Path: {' -> '.join(path)}")
    else:
        print("  No path found")

