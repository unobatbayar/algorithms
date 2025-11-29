"""
Breadth-First Search (BFS) Algorithm

BFS is a graph traversal algorithm that explores all nodes at the present depth
level before moving on to nodes at the next depth level. It uses a queue data
structure to keep track of nodes to visit.

Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V) - for the queue and visited set

Applications:
    - Shortest path in unweighted graphs
    - Level-order traversal of trees
    - Finding connected components
    - Web crawling
"""


from collections import deque


def bfs(graph, start):
    """
    Performs Breadth-First Search on a graph.
    
    Args:
        graph: Dictionary representing adjacency list {node: [neighbors]}
        start: Starting node for BFS
    
    Returns:
        List of nodes visited in BFS order
    """
    visited = []
    queue = deque([start])
    visited_set = {start}
    
    while queue:
        # Dequeue a vertex from queue
        node = queue.popleft()
        visited.append(node)
        
        # Get all adjacent vertices of the dequeued node
        # If an adjacent hasn't been visited, mark it and enqueue it
        for neighbor in graph.get(node, []):
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)
    
    return visited


def bfs_shortest_path(graph, start, end):
    """
    Finds the shortest path between two nodes using BFS.
    
    Args:
        graph: Dictionary representing adjacency list
        start: Starting node
        end: Target node
    
    Returns:
        List representing shortest path from start to end, or None if no path exists
    """
    if start == end:
        return [start]
    
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        node, path = queue.popleft()
        
        for neighbor in graph.get(node, []):
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
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
    
    print("BFS traversal starting from 'A':")
    result = bfs(graph, 'A')
    print(result)
    
    print("\nShortest path from 'A' to 'F':")
    path = bfs_shortest_path(graph, 'A', 'F')
    print(path)

