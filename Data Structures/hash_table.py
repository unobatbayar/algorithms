"""
Hash Table (Hash Map) Data Structure

A hash table is a data structure that implements an associative array,
mapping keys to values using a hash function to compute an index.

Time Complexity (average case):
    - Insertion: O(1)
    - Deletion: O(1)
    - Search: O(1)

Time Complexity (worst case): O(n) - when all keys hash to same bucket

Space Complexity: O(n)

Note: Uses chaining to handle collisions.
"""


class HashTable:
    """Hash table implementation using chaining for collision resolution."""
    
    def __init__(self, capacity=10):
        """
        Initialize hash table.
        
        Args:
            capacity: Initial capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
    
    def _hash(self, key):
        """Compute hash value for a key."""
        if isinstance(key, int):
            return key % self.capacity
        # For string keys, use sum of character codes
        return sum(ord(c) for c in str(key)) % self.capacity
    
    def insert(self, key, value):
        """Insert or update key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Add new key-value pair
        bucket.append((key, value))
        self.size += 1
        
        # Resize if load factor > 0.7
        if self.size > self.capacity * 0.7:
            self._resize()
    
    def get(self, key):
        """Get value for a key."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """Delete key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        
        return False
    
    def contains(self, key):
        """Check if key exists."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def _resize(self):
        """Resize hash table when load factor is too high."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        # Rehash all elements
        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)
    
    def __len__(self):
        """Return number of key-value pairs."""
        return self.size
    
    def __str__(self):
        """String representation."""
        items = []
        for bucket in self.buckets:
            for key, value in bucket:
                items.append(f"{key}: {value}")
        return "{" + ", ".join(items) + "}"


# Example usage
if __name__ == "__main__":
    ht = HashTable()
    
    print("Inserting key-value pairs:")
    ht.insert("apple", 5)
    ht.insert("banana", 3)
    ht.insert("cherry", 8)
    print(f"  {ht}")
    print(f"  Size: {len(ht)}")
    
    print("\nGetting values:")
    print(f"  apple: {ht.get('apple')}")
    print(f"  banana: {ht.get('banana')}")
    
    print(f"\nContains 'cherry': {ht.contains('cherry')}")
    print(f"Contains 'date': {ht.contains('date')}")
    
    print("\nDeleting 'banana':")
    ht.delete("banana")
    print(f"  {ht}")
    print(f"  Size: {len(ht)}")

