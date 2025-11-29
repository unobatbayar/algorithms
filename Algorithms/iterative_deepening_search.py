"""
Iterative Deepening Search (IDS) Algorithm

IDS combines the benefits of BFS (optimality) and DFS (space efficiency).
It performs DFS with increasing depth limits until the goal is found.

Time Complexity: O(b^d) where b is branching factor, d is depth
Space Complexity: O(bd) - much better than BFS which is O(b^d)

Advantages:
    - Optimal (finds shortest path)
    - Space efficient (like DFS)
    - Complete (will find solution if it exists)
"""


def iterative_deepening_search(graph, start, goal):
    """
    Finds path from start to goal using Iterative Deepening Search.
    
    Args:
        graph: Dictionary representing adjacency list {node: [neighbors]}
        start: Starting node
        goal: Target node
    
    Returns:
        Path from start to goal, or None if no path exists
    """
    depth = 0
    
    while True:
        result = depth_limited_search(graph, start, goal, depth)
        if result is not None:
            return result
        depth += 1


def depth_limited_search(graph, start, goal, max_depth, path=None, visited=None):
    """
    Performs DFS with a depth limit.
    
    Args:
        graph: Dictionary representing adjacency list
        start: Current node
        goal: Target node
        max_depth: Maximum depth to search
        path: Current path being explored
        visited: Set of visited nodes at current depth
    
    Returns:
        Path if goal found, None otherwise
    """
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    if start == goal:
        return path + [start]
    
    if max_depth == 0:
        return None
    
    visited.add(start)
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = depth_limited_search(
                graph, neighbor, goal, max_depth - 1, path + [start], visited.copy()
            )
            if result is not None:
                return result
    
    return None


# Example usage
if __name__ == "__main__":
    # Example graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("Iterative Deepening Search from 'A' to 'F':")
    path = iterative_deepening_search(graph, 'A', 'F')
    
    if path:
        print(f"  Path found: {' -> '.join(path)}")
    else:
        print("  No path found")

