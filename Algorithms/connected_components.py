"""
Connected Components in a Graph

A connected component is a subgraph in which any two vertices are connected
by paths, and which is connected to no additional vertices in the supergraph.

This algorithm finds all connected components in an undirected graph using DFS.

Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V)
"""


def find_connected_components(graph):
    """
    Finds all connected components in an undirected graph.
    
    Args:
        graph: Dictionary representing adjacency list {node: [neighbors]}
    
    Returns:
        List of components, where each component is a list of vertices
    """
    visited = set()
    components = []
    
    def dfs(node, component):
        """DFS helper to explore a connected component."""
        visited.add(node)
        component.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, component)
    
    # Find all components
    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)
    
    return components


def count_connected_components(graph):
    """
    Counts the number of connected components in a graph.
    
    Args:
        graph: Dictionary representing adjacency list
    
    Returns:
        Number of connected components
    """
    return len(find_connected_components(graph))


# Example usage
if __name__ == "__main__":
    # Example graph with 3 connected components
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B'],
        'D': ['E'],
        'E': ['D'],
        'F': []
    }
    
    print("Connected components:")
    components = find_connected_components(graph)
    
    for i, component in enumerate(components, 1):
        print(f"  Component {i}: {component}")
    
    print(f"\nTotal number of components: {count_connected_components(graph)}")

