"""
Trie (Prefix Tree) Data Structure

A trie is a tree-like data structure used to store a dynamic set of strings,
where the keys are usually strings. It's efficient for prefix-based searches.

Time Complexity:
    - Insertion: O(m) where m is length of string
    - Search: O(m)
    - Prefix search: O(m)

Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of strings, M is average length

Applications:
    - Autocomplete
    - Spell checker
    - IP routing
    - Prefix matching
"""


class TrieNode:
    """Node class for trie."""
    
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """Trie (Prefix Tree) implementation."""
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
    
    def search(self, word):
        """Search for a word in the trie."""
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """Check if any word in trie starts with the given prefix."""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
    
    def delete(self, word):
        """Delete a word from the trie."""
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            child_node = node.children[char]
            should_delete = _delete(child_node, word, index + 1)
            
            if should_delete:
                del node.children[char]
                return len(node.children) == 0
            
            return False
        
        _delete(self.root, word, 0)
    
    def get_all_words(self, prefix=""):
        """Get all words with given prefix."""
        node = self.root
        
        # Navigate to prefix node
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Collect all words from this node
        words = []
        
        def _collect(node, current_word):
            if node.is_end_of_word:
                words.append(prefix + current_word)
            
            for char, child_node in node.children.items():
                _collect(child_node, current_word + char)
        
        _collect(node, "")
        return words


# Example usage
if __name__ == "__main__":
    trie = Trie()
    
    print("Inserting words:")
    words = ["apple", "app", "application", "apply", "banana", "band"]
    for word in words:
        trie.insert(word)
        print(f"  Inserted: {word}")
    
    print("\nSearching:")
    print(f"  'app': {trie.search('app')}")
    print(f"  'apple': {trie.search('apple')}")
    print(f"  'appl': {trie.search('appl')}")
    
    print("\nPrefix search:")
    print(f"  Starts with 'app': {trie.starts_with('app')}")
    print(f"  Starts with 'ban': {trie.starts_with('ban')}")
    print(f"  Starts with 'xyz': {trie.starts_with('xyz')}")
    
    print("\nAll words with prefix 'app':")
    print(f"  {trie.get_all_words('app')}")
    
    print("\nDeleting 'app':")
    trie.delete('app')
    print(f"  'app' exists: {trie.search('app')}")
    print(f"  'apple' exists: {trie.search('apple')}")

