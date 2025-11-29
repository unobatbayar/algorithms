"""
Knuth-Morris-Pratt (KMP) String Matching Algorithm

KMP is an efficient string matching algorithm that finds occurrences of a pattern
in a text. It uses the concept of longest proper prefix which is also a suffix (LPS)
to avoid unnecessary comparisons.

Time Complexity: O(n + m) where n is text length and m is pattern length
Space Complexity: O(m)

More efficient than naive string matching which is O(n * m).
"""


def compute_lps(pattern):
    """
    Compute Longest Proper Prefix which is also Suffix (LPS) array.
    
    Args:
        pattern: Pattern string
    
    Returns:
        LPS array
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of previous longest prefix suffix
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps


def kmp_search(text, pattern):
    """
    Search for pattern in text using KMP algorithm.
    
    Args:
        text: Text string to search in
        pattern: Pattern string to search for
    
    Returns:
        List of indices where pattern is found
    """
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return []
    
    lps = compute_lps(pattern)
    result = []
    
    i = 0  # Index for text
    j = 0  # Index for pattern
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            # Pattern found at index i - j
            result.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            # Mismatch after j matches
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return result


# Example usage
if __name__ == "__main__":
    text = "ABABDABACDABABCABCAB"
    pattern = "ABABCABAB"
    
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    
    matches = kmp_search(text, pattern)
    print(f"\nPattern found at indices: {matches}")
    
    if matches:
        print("Matches:")
        for idx in matches:
            print(f"  Position {idx}: {text[idx:idx+len(pattern)]}")

