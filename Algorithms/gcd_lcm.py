"""
Greatest Common Divisor (GCD) and Least Common Multiple (LCM)

GCD: The largest positive integer that divides both numbers without remainder.
LCM: The smallest positive integer that is divisible by both numbers.

Euclidean Algorithm is used for efficient GCD computation.

Time Complexity: O(log(min(a, b)))
Space Complexity: O(1)
"""


def gcd_euclidean(a, b):
    """
    Computes GCD using Euclidean algorithm (iterative).
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        GCD of a and b
    """
    while b:
        a, b = b, a % b
    return abs(a)


def gcd_recursive(a, b):
    """
    Computes GCD using Euclidean algorithm (recursive).
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        GCD of a and b
    """
    if b == 0:
        return abs(a)
    return gcd_recursive(b, a % b)


def lcm(a, b):
    """
    Computes LCM using the relationship: LCM(a, b) = |a * b| / GCD(a, b)
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        LCM of a and b
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd_euclidean(a, b)


def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm: finds GCD and coefficients x, y such that
    ax + by = gcd(a, b)
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        Tuple (gcd, x, y) where gcd is GCD and ax + by = gcd
    """
    if a == 0:
        return abs(b), 0, 1 if b >= 0 else -1
    
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y


# Example usage
if __name__ == "__main__":
    a, b = 48, 18
    
    print(f"GCD({a}, {b}):")
    print(f"  Euclidean (iterative): {gcd_euclidean(a, b)}")
    print(f"  Euclidean (recursive): {gcd_recursive(a, b)}")
    
    print(f"\nLCM({a}, {b}): {lcm(a, b)}")
    
    print(f"\nExtended GCD({a}, {b}):")
    gcd, x, y = extended_gcd(a, b)
    print(f"  GCD: {gcd}")
    print(f"  Coefficients: {a}*{x} + {b}*{y} = {gcd}")

