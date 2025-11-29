"""
Binary Tree Data Structure

A binary tree is a tree data structure where each node has at most two children,
referred to as the left child and right child.

Time Complexity:
    - Insertion: O(n) worst case
    - Search: O(n) worst case
    - Traversal: O(n)

Space Complexity: O(n)

Note: This is a basic binary tree. For better performance, use Binary Search Tree.
"""


class TreeNode:
    """Node class for binary tree."""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """Binary tree implementation."""
    
    def __init__(self):
        self.root = None
    
    def insert_level_order(self, data):
        """Insert node using level-order insertion (BFS approach)."""
        new_node = TreeNode(data)
        
        if self.root is None:
            self.root = new_node
            return
        
        from collections import deque
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            
            if node.left is None:
                node.left = new_node
                return
            else:
                queue.append(node.left)
            
            if node.right is None:
                node.right = new_node
                return
            else:
                queue.append(node.right)
    
    def inorder_traversal(self, node=None):
        """In-order traversal: Left -> Root -> Right."""
        if node is None:
            node = self.root
        
        result = []
        
        def traverse(n):
            if n:
                traverse(n.left)
                result.append(n.data)
                traverse(n.right)
        
        traverse(node)
        return result
    
    def preorder_traversal(self, node=None):
        """Pre-order traversal: Root -> Left -> Right."""
        if node is None:
            node = self.root
        
        result = []
        
        def traverse(n):
            if n:
                result.append(n.data)
                traverse(n.left)
                traverse(n.right)
        
        traverse(node)
        return result
    
    def postorder_traversal(self, node=None):
        """Post-order traversal: Left -> Right -> Root."""
        if node is None:
            node = self.root
        
        result = []
        
        def traverse(n):
            if n:
                traverse(n.left)
                traverse(n.right)
                result.append(n.data)
        
        traverse(node)
        return result
    
    def level_order_traversal(self):
        """Level-order traversal (BFS): Level by level."""
        if self.root is None:
            return []
        
        from collections import deque
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self, node=None):
        """Calculate height of the tree."""
        if node is None:
            node = self.root
        
        if node is None:
            return -1
        
        return 1 + max(self.height(node.left), self.height(node.right))


# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    
    print("Inserting elements:")
    for i in [1, 2, 3, 4, 5, 6, 7]:
        tree.insert_level_order(i)
    
    print(f"In-order: {tree.inorder_traversal()}")
    print(f"Pre-order: {tree.preorder_traversal()}")
    print(f"Post-order: {tree.postorder_traversal()}")
    print(f"Level-order: {tree.level_order_traversal()}")
    print(f"Height: {tree.height()}")

