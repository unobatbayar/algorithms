"""
Graph Data Structure

A graph is a collection of nodes (vertices) connected by edges.
Can be directed or undirected, weighted or unweighted.

Time Complexity:
    - Add vertex: O(1)
    - Add edge: O(1)
    - Remove vertex: O(V + E)
    - Remove edge: O(E)
    - Check edge: O(1) for adjacency list, O(1) for adjacency matrix

Space Complexity: O(V + E) for adjacency list, O(V²) for adjacency matrix

This implementation uses adjacency list representation.
"""


class Graph:
    """Graph implementation using adjacency list."""
    
    def __init__(self, directed=False):
        """
        Initialize graph.
        
        Args:
            directed: True for directed graph, False for undirected
        """
        self.graph = {}
        self.directed = directed
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, u, v, weight=1):
        """
        Add an edge between vertices u and v.
        
        Args:
            u: First vertex
            v: Second vertex
            weight: Edge weight (default: 1)
        """
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        
        self.graph[u].append((v, weight))
        
        # If undirected, add reverse edge
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def remove_edge(self, u, v):
        """Remove edge between u and v."""
        if u in self.graph:
            self.graph[u] = [(vertex, weight) for vertex, weight in self.graph[u]
                            if vertex != v]
        
        if not self.directed and v in self.graph:
            self.graph[v] = [(vertex, weight) for vertex, weight in self.graph[v]
                            if vertex != u]
    
    def remove_vertex(self, vertex):
        """Remove a vertex and all its edges."""
        if vertex in self.graph:
            del self.graph[vertex]
        
        # Remove edges pointing to this vertex
        for v in self.graph:
            self.graph[v] = [(u, w) for u, w in self.graph[v] if u != vertex]
    
    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex."""
        return self.graph.get(vertex, [])
    
    def get_vertices(self):
        """Get all vertices in the graph."""
        return list(self.graph.keys())
    
    def get_edges(self):
        """Get all edges in the graph."""
        edges = []
        visited = set()
        
        for u in self.graph:
            for v, weight in self.graph[u]:
                if not self.directed:
                    # For undirected, only add each edge once
                    edge_key = tuple(sorted([u, v]))
                    if edge_key not in visited:
                        edges.append((u, v, weight))
                        visited.add(edge_key)
                else:
                    edges.append((u, v, weight))
        
        return edges
    
    def __str__(self):
        """String representation of the graph."""
        result = []
        for vertex in self.graph:
            neighbors = [f"{v}({w})" for v, w in self.graph[vertex]]
            result.append(f"{vertex}: {', '.join(neighbors)}")
        return "\n".join(result)


# Example usage
if __name__ == "__main__":
    # Undirected graph
    print("Undirected Graph:")
    g = Graph(directed=False)
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    
    print(g)
    print(f"\nVertices: {g.get_vertices()}")
    print(f"Edges: {g.get_edges()}")
    print(f"Neighbors of 'B': {g.get_neighbors('B')}")
    
    # Directed graph
    print("\n\nDirected Graph:")
    dg = Graph(directed=True)
    dg.add_edge('A', 'B', 4)
    dg.add_edge('A', 'C', 2)
    dg.add_edge('B', 'D', 5)
    
    print(dg)
    print(f"Edges: {dg.get_edges()}")

