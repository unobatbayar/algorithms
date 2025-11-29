"""
Dijkstra's Shortest Path Algorithm

Dijkstra's algorithm finds the shortest paths from a source vertex to all other
vertices in a weighted graph with non-negative edge weights. It uses a greedy
approach, always selecting the vertex with the minimum distance.

Time Complexity: O((V + E) log V) with priority queue, O(V²) with array
Space Complexity: O(V)

Note: Does not work with negative edge weights. Use Bellman-Ford for that.
"""


import heapq


def dijkstra(graph, start):
    """
    Finds shortest paths from start vertex to all other vertices.
    
    Args:
        graph: Dictionary representing weighted graph {node: [(neighbor, weight), ...]}
        start: Starting vertex
    
    Returns:
        Dictionary of shortest distances {vertex: distance}
    """
    # Initialize distances: all vertices start at infinity except start (0)
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        # Get vertex with minimum distance
        current_dist, current_vertex = heapq.heappop(pq)
        
        # Skip if already processed
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        # Update distances to neighbors
        for neighbor, weight in graph.get(current_vertex, []):
            if neighbor in visited:
                continue
            
            distance = current_dist + weight
            
            # If found shorter path, update and add to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


def dijkstra_path(graph, start, end):
    """
    Finds shortest path from start to end vertex.
    
    Args:
        graph: Dictionary representing weighted graph
        start: Starting vertex
        end: Target vertex
    
    Returns:
        Tuple (distance, path) where path is list of vertices
    """
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        # Early termination if reached target
        if current_vertex == end:
            break
        
        for neighbor, weight in graph.get(current_vertex, []):
            if neighbor in visited:
                continue
            
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct path
    if distances[end] == float('infinity'):
        return None, None
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return distances[end], path


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
    
    print("Shortest distances from 'A':")
    distances = dijkstra(graph, 'A')
    for vertex, distance in distances.items():
        print(f"  {vertex}: {distance}")
    
    print("\nShortest path from 'A' to 'E':")
    dist, path = dijkstra_path(graph, 'A', 'E')
    print(f"  Distance: {dist}")
    print(f"  Path: {' -> '.join(path)}")

