"""
Binary Search Tree (BST) Data Structure

A Binary Search Tree is a binary tree where for each node:
- All nodes in left subtree have values < node's value
- All nodes in right subtree have values > node's value
- Left and right subtrees are also BSTs

Time Complexity:
    - Search: O(log n) average, O(n) worst case
    - Insertion: O(log n) average, O(n) worst case
    - Deletion: O(log n) average, O(n) worst case
    - Traversal: O(n)

Space Complexity: O(n)

Note: Performance depends on tree balance. For guaranteed O(log n), use AVL or Red-Black trees.
"""


class TreeNode:
    """Node class for BST."""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree implementation."""
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """Insert a value into the BST."""
        self.root = self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Recursive helper for insertion."""
        if node is None:
            return TreeNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        # If data == node.data, do nothing (no duplicates)
        
        return node
    
    def search(self, data):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        """Recursive helper for search."""
        if node is None or node.data == data:
            return node
        
        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def delete(self, data):
        """Delete a value from the BST."""
        self.root = self._delete_recursive(self.root, data)
    
    def _delete_recursive(self, node, data):
        """Recursive helper for deletion."""
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node to delete found
            # Case 1: No child or one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Case 2: Two children - find inorder successor
            node.data = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.data)
        
        return node
    
    def _min_value(self, node):
        """Find minimum value in a subtree."""
        while node.left:
            node = node.left
        return node.data
    
    def inorder_traversal(self):
        """In-order traversal returns sorted values."""
        result = []
        
        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.data)
                traverse(node.right)
        
        traverse(self.root)
        return result
    
    def height(self):
        """Calculate height of the BST."""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Recursive helper for height calculation."""
        if node is None:
            return -1
        return 1 + max(self._height_recursive(node.left),
                      self._height_recursive(node.right))


# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    print("Inserting elements:")
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
        print(f"  Inserted {val}")
    
    print(f"\nIn-order traversal (sorted): {bst.inorder_traversal()}")
    print(f"Height: {bst.height()}")
    
    print("\nSearching for 40:")
    result = bst.search(40)
    print(f"  Found: {result is not None}")
    
    print("\nDeleting 30:")
    bst.delete(30)
    print(f"In-order after deletion: {bst.inorder_traversal()}")

