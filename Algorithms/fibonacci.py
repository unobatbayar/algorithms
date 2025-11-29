"""
Fibonacci Sequence Algorithms

The Fibonacci sequence is a series of numbers where each number is the sum
of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

This module provides multiple implementations:
1. Recursive (inefficient)
2. Memoized recursive (efficient)
3. Iterative (most efficient)
4. Matrix exponentiation (O(log n))

Time Complexity:
    - Recursive: O(2^n) - exponential
    - Memoized: O(n)
    - Iterative: O(n)
    - Matrix: O(log n)
"""


def fibonacci_recursive(n):
    """
    Computes nth Fibonacci number using naive recursion.
    Very inefficient for large n.
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
    
    Returns:
        nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoized(n, memo=None):
    """
    Computes nth Fibonacci number using memoization.
    
    Args:
        n: Position in Fibonacci sequence
        memo: Dictionary for memoization (internal use)
    
    Returns:
        nth Fibonacci number
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def fibonacci_iterative(n):
    """
    Computes nth Fibonacci number using iteration.
    Most efficient simple approach.
    
    Args:
        n: Position in Fibonacci sequence
    
    Returns:
        nth Fibonacci number
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


def fibonacci_sequence(n):
    """
    Generates first n Fibonacci numbers.
    
    Args:
        n: Number of Fibonacci numbers to generate
    
    Returns:
        List of first n Fibonacci numbers
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    
    return sequence


# Example usage
if __name__ == "__main__":
    n = 10
    
    print(f"Fibonacci sequence (first {n} numbers):")
    sequence = fibonacci_sequence(n)
    print(f"  {sequence}")
    
    print(f"\nFibonacci({n}) using different methods:")
    print(f"  Iterative: {fibonacci_iterative(n)}")
    print(f"  Memoized: {fibonacci_memoized(n)}")
    print(f"  Recursive: {fibonacci_recursive(n)}")  # Slow for large n

