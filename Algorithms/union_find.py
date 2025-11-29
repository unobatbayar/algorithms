"""
Union-Find (Disjoint Set Union) Data Structure

Union-Find is a data structure that tracks a set of elements partitioned into
disjoint subsets. It supports two operations:
- Find: Determine which subset an element belongs to
- Union: Join two subsets into a single subset

Time Complexity:
    - With path compression and union by rank: Nearly O(1) amortized
    - Without optimizations: O(n) worst case

Applications:
    - Kruskal's MST algorithm
    - Detecting cycles in graphs
    - Network connectivity
"""


class UnionFind:
    """Union-Find data structure with path compression and union by rank."""
    
    def __init__(self, n):
        """
        Initialize Union-Find with n elements.
        
        Args:
            n: Number of elements (0 to n-1)
        """
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        """
        Find the root of x with path compression.
        
        Args:
            x: Element to find root of
        
        Returns:
            Root of x
        """
        if self.parent[x] != x:
            # Path compression: make parent point directly to root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """
        Union the sets containing x and y.
        
        Args:
            x: First element
            y: Second element
        
        Returns:
            True if union was performed, False if already in same set
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same set
        
        # Union by rank: attach smaller tree under root of larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.components -= 1
        return True
    
    def connected(self, x, y):
        """
        Check if x and y are in the same set.
        
        Args:
            x: First element
            y: Second element
        
        Returns:
            True if connected, False otherwise
        """
        return self.find(x) == self.find(y)
    
    def count_components(self):
        """
        Get the number of connected components.
        
        Returns:
            Number of components
        """
        return self.components


# Example usage
if __name__ == "__main__":
    uf = UnionFind(10)
    
    print("Union operations:")
    print(f"  Union(0, 1): {uf.union(0, 1)}")
    print(f"  Union(2, 3): {uf.union(2, 3)}")
    print(f"  Union(4, 5): {uf.union(4, 5)}")
    print(f"  Union(0, 2): {uf.union(0, 2)}")
    print(f"  Union(0, 1): {uf.union(0, 1)}")  # Already connected
    
    print(f"\nConnected(0, 3): {uf.connected(0, 3)}")
    print(f"Connected(0, 4): {uf.connected(0, 4)}")
    print(f"Number of components: {uf.count_components()}")

