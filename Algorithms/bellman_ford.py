"""
Bellman-Ford Shortest Path Algorithm

Bellman-Ford algorithm finds shortest paths from a source vertex to all other
vertices in a weighted graph. Unlike Dijkstra's, it can handle negative edge
weights and can detect negative cycles.

Time Complexity: O(V * E) where V is vertices and E is edges
Space Complexity: O(V)

Note: Slower than Dijkstra's but more versatile (handles negative weights).
"""


def bellman_ford(graph, start):
    """
    Finds shortest paths from start vertex to all other vertices.
    
    Args:
        graph: Dictionary representing weighted graph {node: [(neighbor, weight), ...]}
        start: Starting vertex
    
    Returns:
        Tuple (distances, has_negative_cycle)
        - distances: Dictionary of shortest distances {vertex: distance}
        - has_negative_cycle: Boolean indicating if negative cycle was detected
    """
    # Get all vertices
    vertices = set(graph.keys())
    for neighbors in graph.values():
        vertices.update(neighbor for neighbor, _ in neighbors)
    
    # Initialize distances: all vertices start at infinity except start (0)
    distances = {vertex: float('infinity') for vertex in vertices}
    distances[start] = 0
    
    # Relax edges V-1 times
    for _ in range(len(vertices) - 1):
        for vertex in graph:
            for neighbor, weight in graph.get(vertex, []):
                if distances[vertex] != float('infinity'):
                    if distances[vertex] + weight < distances[neighbor]:
                        distances[neighbor] = distances[vertex] + weight
    
    # Check for negative cycles
    # If we can still relax edges, there's a negative cycle
    has_negative_cycle = False
    for vertex in graph:
        for neighbor, weight in graph.get(vertex, []):
            if distances[vertex] != float('infinity'):
                if distances[vertex] + weight < distances[neighbor]:
                    has_negative_cycle = True
                    break
        if has_negative_cycle:
            break
    
    return distances, has_negative_cycle


# Example usage
if __name__ == "__main__":
    # Example weighted graph: {node: [(neighbor, weight), ...]}
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
    
    print("Shortest distances from 'A' using Bellman-Ford:")
    distances, has_cycle = bellman_ford(graph, 'A')
    
    if has_cycle:
        print("Warning: Negative cycle detected!")
    else:
        for vertex, distance in distances.items():
            print(f"  {vertex}: {distance}")

