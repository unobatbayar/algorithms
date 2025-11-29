"""
Sieve of Eratosthenes

The Sieve of Eratosthenes is an efficient algorithm to find all prime numbers
up to a given limit. It works by iteratively marking multiples of each prime
starting from 2.

Time Complexity: O(n log log n)
Space Complexity: O(n)
"""


def sieve_of_eratosthenes(n):
    """
    Finds all prime numbers up to n using Sieve of Eratosthenes.
    
    Args:
        n: Upper limit (inclusive)
    
    Returns:
        List of prime numbers up to n
    """
    if n < 2:
        return []
    
    # Create boolean array: is_prime[i] = True if i is prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Sieve: mark multiples of primes as composite
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as composite
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    # Collect all primes
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes


def is_prime(n):
    """
    Checks if a number is prime using trial division.
    More efficient for single number checks.
    
    Args:
        n: Number to check
    
    Returns:
        True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


# Example usage
if __name__ == "__main__":
    n = 50
    
    print(f"Prime numbers up to {n}:")
    primes = sieve_of_eratosthenes(n)
    print(f"  {primes}")
    print(f"  Count: {len(primes)}")
    
    print(f"\nIs {17} prime? {is_prime(17)}")
    print(f"Is {20} prime? {is_prime(20)}")

