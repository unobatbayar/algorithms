"""
Selection Sort Algorithm

Selection Sort finds the minimum element from the unsorted portion of the array
and places it at the beginning. This process is repeated for the remaining elements.

Time Complexity:
    - Best Case: O(n²)
    - Average Case: O(n²)
    - Worst Case: O(n²)

Space Complexity: O(1) - in-place sorting

Stable: No (may change relative order of equal elements)
"""


def selection_sort(arr):
    """
    Sorts an array using the Selection Sort algorithm.
    
    Args:
        arr: List of comparable elements to be sorted (modified in-place)
    
    Returns:
        None (sorts in-place)
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    
    selection_sort(numbers)
    print(f"Sorted array: {numbers}")
