"""
Comb Sort Algorithm

Comb Sort is an improvement over Bubble Sort. It uses a gap larger than 1,
which starts large and shrinks by a factor of 1.3 in each iteration.
The gap continues until it becomes 1, at which point it becomes a regular Bubble Sort.

Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n² / 2^p) where p is number of increments
    - Worst Case: O(n²)

Space Complexity: O(1) - in-place sorting

Stable: No (may change relative order of equal elements)
"""


def comb_sort(arr):
    """
    Sorts an array using the Comb Sort algorithm.
    
    Args:
        arr: List of comparable elements to be sorted (modified in-place)
    
    Returns:
        None (sorts in-place)
    """
    n = len(arr)
    
    # Initialize gap
    gap = n
    
    # Initialize swapped as true to ensure loop runs
    swapped = True
    
    # Keep running while gap is more than 1 or last iteration caused a swap
    while gap != 1 or swapped:
        # Find next gap (shrink factor is 1.3)
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1
        
        # Initialize swapped as false to check if swap happened
        swapped = False
        
        # Compare all elements with current gap
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    
    comb_sort(numbers)
    print(f"Sorted array: {numbers}")
