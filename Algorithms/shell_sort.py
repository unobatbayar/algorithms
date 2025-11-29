"""
Shell Sort Algorithm

Shell Sort is a generalization of Insertion Sort that allows the exchange
of items that are far apart. It starts by sorting pairs of elements far apart
from each other, then progressively reduces the gap between elements to be compared.

Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n^1.5) - depends on gap sequence
    - Worst Case: O(n²)

Space Complexity: O(1) - in-place sorting

Stable: No (may change relative order of equal elements)
"""


def shell_sort(arr):
    """
    Sorts an array using the Shell Sort algorithm.
    
    Args:
        arr: List of comparable elements to be sorted (modified in-place)
    
    Returns:
        None (sorts in-place)
    """
    n = len(arr)
    
    # Start with a large gap, then reduce the gap
    # Using gap sequence: n/2, n/4, n/8, ... until gap = 1
    gap = n // 2
    
    # Do a gapped insertion sort for this gap size
    while gap > 0:
        # Perform insertion sort for elements at gap intervals
        for i in range(gap, n):
            # Store current element
            temp = arr[i]
            
            # Shift earlier gap-sorted elements up until correct position
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Place temp at its correct position
            arr[j] = temp
        
        # Reduce gap for next iteration
        gap //= 2


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    
    shell_sort(numbers)
    print(f"Sorted array: {numbers}")

