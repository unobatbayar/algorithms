"""
Rabin-Karp String Matching Algorithm

Rabin-Karp is a string matching algorithm that uses hashing to find patterns
in text. It compares hash values of the pattern and substrings of the text.

Time Complexity:
    - Average Case: O(n + m) where n is text length and m is pattern length
    - Worst Case: O(n * m) - when hash collisions occur frequently

Space Complexity: O(1)

Note: Uses rolling hash to efficiently compute hash of sliding window.
"""


def rabin_karp_search(text, pattern, base=256, mod=101):
    """
    Search for pattern in text using Rabin-Karp algorithm.
    
    Args:
        text: Text string to search in
        pattern: Pattern string to search for
        base: Base for hash function (default: 256 for ASCII)
        mod: Modulus for hash function (should be prime)
    
    Returns:
        List of indices where pattern is found
    """
    n = len(text)
    m = len(pattern)
    
    if m == 0 or m > n:
        return []
    
    result = []
    
    # Calculate hash of pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    h = 1  # h = base^(m-1) % mod
    
    # Calculate h
    for i in range(m - 1):
        h = (h * base) % mod
    
    # Calculate initial hash values
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        text_hash = (base * text_hash + ord(text[i])) % mod
    
    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == text_hash:
            # Check if characters actually match (to handle hash collisions)
            if text[i:i + m] == pattern:
                result.append(i)
        
        # Calculate hash for next window
        if i < n - m:
            # Remove leading character, add trailing character
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
            
            # Handle negative hash values
            if text_hash < 0:
                text_hash += mod
    
    return result


# Example usage
if __name__ == "__main__":
    text = "ABABDABACDABABCABCAB"
    pattern = "ABABCABAB"
    
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    
    matches = rabin_karp_search(text, pattern)
    print(f"\nPattern found at indices: {matches}")
    
    if matches:
        print("Matches:")
        for idx in matches:
            print(f"  Position {idx}: {text[idx:idx+len(pattern)]}")

