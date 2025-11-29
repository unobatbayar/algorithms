"""
Kruskal's Minimum Spanning Tree Algorithm

Kruskal's algorithm finds a minimum spanning tree (MST) for a connected weighted graph.
It uses a greedy approach: sort all edges by weight, then add edges one by one,
avoiding cycles (using Union-Find data structure).

Time Complexity: O(E log E) or O(E log V) where E is edges and V is vertices
Space Complexity: O(V + E)

The MST connects all vertices with minimum total edge weight.
"""


class UnionFind:
    """Union-Find (Disjoint Set) data structure for cycle detection."""
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        """Find root of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union sets containing x and y."""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same set (would create cycle)
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True


def kruskal_mst(vertices, edges):
    """
    Finds Minimum Spanning Tree using Kruskal's algorithm.
    
    Args:
        vertices: List of vertex labels
        edges: List of tuples (u, v, weight) representing edges
    
    Returns:
        List of edges in the MST: [(u, v, weight), ...]
    """
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Create Union-Find structure
    vertex_to_index = {v: i for i, v in enumerate(vertices)}
    uf = UnionFind(len(vertices))
    
    mst = []
    total_weight = 0
    
    # Process edges in increasing order of weight
    for u, v, weight in edges:
        u_idx = vertex_to_index[u]
        v_idx = vertex_to_index[v]
        
        # If adding this edge doesn't create a cycle, add it to MST
        if uf.union(u_idx, v_idx):
            mst.append((u, v, weight))
            total_weight += weight
            
            # MST has V-1 edges for V vertices
            if len(mst) == len(vertices) - 1:
                break
    
    return mst, total_weight


# Example usage
if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2)
    ]
    
    print("Kruskal's MST:")
    mst, total_weight = kruskal_mst(vertices, edges)
    
    print(f"Total weight: {total_weight}")
    print("Edges in MST:")
    for u, v, weight in mst:
        print(f"  {u} -- {v} (weight: {weight})")

