"""
Depth-First Search (DFS) Algorithm

DFS is a graph traversal algorithm that explores as far as possible along each
branch before backtracking. It uses a stack (or recursion) to keep track of
nodes to visit.

Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V) - for the recursion stack or explicit stack

Applications:
    - Topological sorting
    - Finding connected components
    - Solving puzzles (mazes, sudoku)
    - Detecting cycles in graphs
"""


def dfs(graph, start, visited=None, result=None):
    """
    Performs Depth-First Search on a graph (recursive implementation).
    
    Args:
        graph: Dictionary representing adjacency list {node: [neighbors]}
        start: Starting node for DFS
        visited: Set of visited nodes (internal use)
        result: List to store traversal order (internal use)
    
    Returns:
        List of nodes visited in DFS order
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []
    
    visited.add(start)
    result.append(start)
    
    # Recur for all adjacent vertices
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
    
    return result


def dfs_iterative(graph, start):
    """
    Performs Depth-First Search on a graph (iterative implementation using stack).
    
    Args:
        graph: Dictionary representing adjacency list {node: [neighbors]}
        start: Starting node for DFS
    
    Returns:
        List of nodes visited in DFS order
    """
    visited = []
    stack = [start]
    visited_set = {start}
    
    while stack:
        node = stack.pop()
        visited.append(node)
        
        # Push all unvisited neighbors onto stack
        # Reverse to maintain same order as recursive version
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                stack.append(neighbor)
    
    return visited


def dfs_path(graph, start, end, path=None, visited=None):
    """
    Finds a path between two nodes using DFS.
    
    Args:
        graph: Dictionary representing adjacency list
        start: Starting node
        end: Target node
        path: Current path being explored (internal use)
        visited: Set of visited nodes (internal use)
    
    Returns:
        List representing path from start to end, or None if no path exists
    """
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    path.append(start)
    visited.add(start)
    
    if start == end:
        return path
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, end, path[:], visited.copy())
            if result:
                return result
    
    return None  # No path found


# Example usage
if __name__ == "__main__":
    # Example graph: {node: [neighbors]}
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("DFS traversal (recursive) starting from 'A':")
    result = dfs(graph, 'A')
    print(result)
    
    print("\nDFS traversal (iterative) starting from 'A':")
    result_iter = dfs_iterative(graph, 'A')
    print(result_iter)
    
    print("\nPath from 'A' to 'F' using DFS:")
    path = dfs_path(graph, 'A', 'F')
    print(path)

