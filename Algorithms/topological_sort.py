"""
Topological Sort Algorithm

Topological sort is a linear ordering of vertices in a Directed Acyclic Graph (DAG)
such that for every directed edge (u, v), vertex u comes before v in the ordering.

Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V)

Applications:
    - Task scheduling
    - Build systems (dependency resolution)
    - Course prerequisites
"""


from collections import deque


def topological_sort_kahn(graph):
    """
    Topological sort using Kahn's algorithm (BFS-based).
    
    Args:
        graph: Dictionary representing DAG {node: [neighbors]}
    
    Returns:
        List of vertices in topological order, or None if cycle exists
    """
    # Calculate in-degree for each vertex
    in_degree = {v: 0 for v in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1
    
    # Initialize queue with vertices having no incoming edges
    queue = deque([v for v in in_degree if in_degree[v] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        # Reduce in-degree of neighbors
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # Check if all vertices were processed (no cycle)
    if len(result) != len(in_degree):
        return None  # Cycle detected
    
    return result


def topological_sort_dfs(graph):
    """
    Topological sort using DFS.
    
    Args:
        graph: Dictionary representing DAG {node: [neighbors]}
    
    Returns:
        List of vertices in topological order, or None if cycle exists
    """
    visited = set()
    temp_mark = set()  # For cycle detection
    result = []
    
    def visit(node):
        """DFS visit function."""
        if node in temp_mark:
            return False  # Cycle detected
        if node in visited:
            return True
        
        temp_mark.add(node)
        
        for neighbor in graph.get(node, []):
            if not visit(neighbor):
                return False
        
        temp_mark.remove(node)
        visited.add(node)
        result.append(node)
        return True
    
    # Visit all nodes
    for node in graph:
        if node not in visited:
            if not visit(node):
                return None  # Cycle detected
    
    result.reverse()
    return result


# Example usage
if __name__ == "__main__":
    # Example DAG (course prerequisites)
    graph = {
        'C1': ['C3'],
        'C2': ['C3'],
        'C3': ['C4'],
        'C4': [],
        'C5': ['C4']
    }
    
    print("Topological sort (Kahn's algorithm):")
    result = topological_sort_kahn(graph)
    if result:
        print(f"  {result}")
    else:
        print("  Cycle detected!")
    
    print("\nTopological sort (DFS):")
    result = topological_sort_dfs(graph)
    if result:
        print(f"  {result}")
    else:
        print("  Cycle detected!")

