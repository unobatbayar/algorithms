"""
Uniform Cost Search (UCS) Algorithm

Uniform Cost Search is a variant of Dijkstra's algorithm that finds the
shortest path in a weighted graph. It explores nodes in order of their
path cost from the start node.

Time Complexity: O((V + E) log V) where V is vertices and E is edges
Space Complexity: O(V)

Note: UCS is essentially Dijkstra's algorithm when all edge weights are positive.
The main difference is in terminology and application context.
"""


import heapq


def uniform_cost_search(graph, start, goal):
    """
    Finds shortest path from start to goal using Uniform Cost Search.
    
    Args:
        graph: Dictionary representing weighted graph {node: [(neighbor, weight), ...]}
        start: Starting node
        goal: Target node
    
    Returns:
        Tuple (cost, path) where path is list of nodes, or (None, None) if no path
    """
    # Priority queue: (cost, node, path)
    pq = [(0, start, [start])]
    visited = set()
    
    while pq:
        cost, current, path = heapq.heappop(pq)
        
        # Skip if already visited with lower cost
        if current in visited:
            continue
        
        visited.add(current)
        
        # Goal reached
        if current == goal:
            return cost, path
        
        # Explore neighbors
        for neighbor, edge_weight in graph.get(current, []):
            if neighbor not in visited:
                new_cost = cost + edge_weight
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))
    
    return None, None  # No path found


# Example usage
if __name__ == "__main__":
    # Example weighted graph
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
    
    print("Uniform Cost Search from 'A' to 'E':")
    cost, path = uniform_cost_search(graph, 'A', 'E')
    
    if path:
        print(f"  Cost: {cost}")
        print(f"  Path: {' -> '.join(path)}")
    else:
        print("  No path found")

