"""
Prim's Minimum Spanning Tree Algorithm

Prim's algorithm finds a minimum spanning tree (MST) for a connected weighted graph.
It starts from an arbitrary vertex and grows the MST by adding the minimum-weight
edge that connects a vertex in the MST to a vertex outside the MST.

Time Complexity: O(E log V) with binary heap, O(V²) with array
Space Complexity: O(V)

The MST connects all vertices with minimum total edge weight.
"""


import heapq


def prim_mst(graph, start):
    """
    Finds Minimum Spanning Tree using Prim's algorithm.
    
    Args:
        graph: Dictionary representing weighted graph {node: [(neighbor, weight), ...]}
        start: Starting vertex
    
    Returns:
        Tuple (mst_edges, total_weight)
        - mst_edges: List of edges in MST: [(u, v, weight), ...]
        - total_weight: Total weight of MST
    """
    mst_edges = []
    visited = {start}
    
    # Priority queue: (weight, from_vertex, to_vertex)
    pq = []
    
    # Initialize with edges from start vertex
    for neighbor, weight in graph.get(start, []):
        heapq.heappush(pq, (weight, start, neighbor))
    
    total_weight = 0
    
    while pq and len(visited) < len(graph):
        weight, u, v = heapq.heappop(pq)
        
        # Skip if both vertices already in MST
        if v in visited:
            continue
        
        # Add edge to MST
        visited.add(v)
        mst_edges.append((u, v, weight))
        total_weight += weight
        
        # Add edges from newly added vertex
        for neighbor, edge_weight in graph.get(v, []):
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, v, neighbor))
    
    return mst_edges, total_weight


# Example usage
if __name__ == "__main__":
    # Example weighted graph: {node: [(neighbor, weight), ...]}
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    
    print("Prim's MST starting from 'A':")
    mst, total_weight = prim_mst(graph, 'A')
    
    print(f"Total weight: {total_weight}")
    print("Edges in MST:")
    for u, v, weight in mst:
        print(f"  {u} -- {v} (weight: {weight})")

