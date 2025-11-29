"""
Ford-Fulkerson Algorithm for Maximum Flow / Minimum Cut

The Ford-Fulkerson algorithm finds the maximum flow in a flow network.
It uses the concept of residual graphs and augmenting paths.

Time Complexity: O(E * max_flow) where E is edges
Space Complexity: O(V + E)

The max-flow min-cut theorem states that the maximum flow equals the minimum cut.
"""


from collections import deque


def bfs_path(graph, source, sink, parent):
    """
    BFS to find augmenting path in residual graph.
    
    Args:
        graph: Residual graph (adjacency list with capacities)
        source: Source vertex
        sink: Sink vertex
        parent: Array to store path
    
    Returns:
        True if path exists, False otherwise
    """
    visited = {source}
    queue = deque([source])
    
    while queue:
        u = queue.popleft()
        
        for v, capacity in graph.get(u, {}).items():
            if v not in visited and capacity > 0:
                visited.add(v)
                parent[v] = u
                queue.append(v)
                if v == sink:
                    return True
    
    return False


def ford_fulkerson(graph, source, sink):
    """
    Finds maximum flow from source to sink using Ford-Fulkerson algorithm.
    
    Args:
        graph: Dictionary representing flow network {u: {v: capacity, ...}, ...}
        source: Source vertex
        sink: Sink vertex
    
    Returns:
        Maximum flow value
    """
    # Create residual graph (initially same as original graph)
    residual = {}
    for u in graph:
        residual[u] = {}
        for v, capacity in graph[u].items():
            residual[u][v] = capacity
            if v not in residual:
                residual[v] = {}
            residual[v][u] = 0  # Reverse edge with 0 capacity
    
    max_flow = 0
    parent = {}
    
    # Augment flow while there is a path from source to sink
    while bfs_path(residual, source, sink, parent):
        # Find minimum residual capacity along the path
        path_flow = float('infinity')
        v = sink
        
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u
        
        # Update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u
        
        max_flow += path_flow
    
    return max_flow


# Example usage
if __name__ == "__main__":
    # Example flow network: {source: {destination: capacity, ...}, ...}
    graph = {
        'S': {'A': 10, 'B': 5},
        'A': {'C': 8, 'D': 2},
        'B': {'C': 4, 'D': 7},
        'C': {'T': 10},
        'D': {'T': 10},
        'T': {}
    }
    
    print("Maximum flow from 'S' to 'T':")
    max_flow = ford_fulkerson(graph, 'S', 'T')
    print(f"  Maximum flow: {max_flow}")

