"""
Floyd-Warshall All-Pairs Shortest Path Algorithm

Floyd-Warshall algorithm finds shortest paths between all pairs of vertices
in a weighted graph. It works with both positive and negative edge weights
(but no negative cycles).

Time Complexity: O(V³) where V is number of vertices
Space Complexity: O(V²)

Note: More efficient than running Dijkstra's or Bellman-Ford for each vertex
when you need all-pairs shortest paths.
"""


def floyd_warshall(graph):
    """
    Finds shortest paths between all pairs of vertices.
    
    Args:
        graph: Dictionary representing weighted graph {node: [(neighbor, weight), ...]}
    
    Returns:
        Dictionary of shortest distances {(u, v): distance}
    """
    # Get all vertices
    vertices = set(graph.keys())
    for neighbors in graph.values():
        vertices.update(neighbor for neighbor, _ in neighbors)
    
    vertices = sorted(list(vertices))
    n = len(vertices)
    
    # Initialize distance matrix
    # dist[i][j] = distance from vertices[i] to vertices[j]
    dist = [[float('infinity')] * n for _ in range(n)]
    
    # Distance from vertex to itself is 0
    for i in range(n):
        dist[i][i] = 0
    
    # Initialize with direct edges
    vertex_to_index = {v: i for i, v in enumerate(vertices)}
    for vertex in graph:
        i = vertex_to_index[vertex]
        for neighbor, weight in graph.get(vertex, []):
            j = vertex_to_index[neighbor]
            dist[i][j] = weight
    
    # Floyd-Warshall algorithm: try all intermediate vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If going through vertex k gives shorter path, update
                if dist[i][k] != float('infinity') and dist[k][j] != float('infinity'):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    
    # Convert to dictionary format
    result = {}
    for i in range(n):
        for j in range(n):
            if dist[i][j] != float('infinity'):
                result[(vertices[i], vertices[j])] = dist[i][j]
    
    return result


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
    
    print("All-pairs shortest distances using Floyd-Warshall:")
    distances = floyd_warshall(graph)
    
    for (u, v), distance in sorted(distances.items()):
        print(f"  {u} -> {v}: {distance}")

