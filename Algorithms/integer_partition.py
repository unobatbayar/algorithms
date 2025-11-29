"""
Integer Partition Algorithm

An integer partition of a positive integer n is a way of writing n as a sum
of positive integers. The order of summands does not matter.

For example, partitions of 4:
    4 = 4
    4 = 3 + 1
    4 = 2 + 2
    4 = 2 + 1 + 1
    4 = 1 + 1 + 1 + 1

This algorithm counts the number of partitions and can generate all partitions.

Time Complexity: O(n * k) where k is number of partitions
Space Complexity: O(n)
"""


def count_partitions(n):
    """
    Counts the number of ways to partition n using dynamic programming.
    
    Args:
        n: Positive integer to partition
    
    Returns:
        Number of partitions of n
    """
    # dp[i] = number of partitions of i
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to partition 0 (empty partition)
    
    # For each number from 1 to n
    for i in range(1, n + 1):
        # For each possible sum j
        for j in range(i, n + 1):
            # Add ways to partition (j - i) using numbers up to i
            dp[j] += dp[j - i]
    
    return dp[n]


def generate_partitions(n):
    """
    Generates all partitions of n.
    
    Args:
        n: Positive integer to partition
    
    Returns:
        List of all partitions (each partition is a list of integers)
    """
    partitions = []
    
    def _generate(current_partition, remaining, start):
        """Helper function to generate partitions recursively."""
        if remaining == 0:
            partitions.append(current_partition[:])
            return
        
        # Try all possible next parts (from start to remaining)
        for i in range(start, remaining + 1):
            current_partition.append(i)
            _generate(current_partition, remaining - i, i)
            current_partition.pop()  # Backtrack
    
    _generate([], n, 1)
    return partitions


# Example usage
if __name__ == "__main__":
    n = 5
    
    print(f"Integer Partitions of {n}:")
    count = count_partitions(n)
    print(f"  Total number of partitions: {count}")
    
    partitions = generate_partitions(n)
    print(f"\n  All partitions:")
    for i, partition in enumerate(partitions, 1):
        print(f"    {i}. {' + '.join(map(str, partition))} = {n}")

