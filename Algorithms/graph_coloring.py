"""
Graph Coloring Algorithm

Graph coloring is the problem of assigning colors to vertices of a graph
such that no two adjacent vertices have the same color. This implementation
uses a greedy approach.

Time Complexity: O(V² + E) where V is vertices and E is edges
Space Complexity: O(V)

The minimum number of colors needed is called the chromatic number.
"""


def graph_coloring(graph):
    """
    Colors a graph using greedy algorithm.
    
    Args:
        graph: Dictionary representing adjacency list {node: [neighbors]}
    
    Returns:
        Dictionary mapping vertices to colors {vertex: color}
    """
    colors = {}
    
    # Sort vertices by degree (descending) for better coloring
    vertices = sorted(graph.keys(), key=lambda v: len(graph.get(v, [])), reverse=True)
    
    for vertex in vertices:
        # Find colors used by adjacent vertices
        used_colors = {colors[neighbor] for neighbor in graph.get(vertex, [])
                      if neighbor in colors}
        
        # Find the smallest color not used by neighbors
        color = 0
        while color in used_colors:
            color += 1
        
        colors[vertex] = color
    
    return colors


def is_valid_coloring(graph, colors):
    """
    Checks if a coloring is valid (no two adjacent vertices have same color).
    
    Args:
        graph: Dictionary representing adjacency list
        colors: Dictionary mapping vertices to colors
    
    Returns:
        True if coloring is valid, False otherwise
    """
    for vertex in graph:
        for neighbor in graph.get(vertex, []):
            if colors.get(vertex) == colors.get(neighbor):
                return False
    return True


# Example usage
if __name__ == "__main__":
    # Example graph
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D'],
        'D': ['A', 'C']
    }
    
    print("Graph coloring:")
    colors = graph_coloring(graph)
    
    for vertex, color in colors.items():
        print(f"  {vertex}: Color {color}")
    
    print(f"\nValid coloring: {is_valid_coloring(graph, colors)}")
    print(f"Number of colors used: {max(colors.values()) + 1}")

