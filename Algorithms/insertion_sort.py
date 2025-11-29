"""
Insertion Sort Algorithm

Insertion Sort builds the final sorted array one item at a time.
It is much less efficient on large lists than more advanced algorithms,
but provides several advantages: simple implementation, efficient for small data sets,
and adaptive (efficient for data sets that are already substantially sorted).

Time Complexity:
    - Best Case: O(n) - when array is already sorted
    - Average Case: O(n²)
    - Worst Case: O(n²)

Space Complexity: O(1) - in-place sorting

Stable: Yes (maintains relative order of equal elements)
"""


def insertion_sort(arr):
    """
    Sorts an array using the Insertion Sort algorithm.
    
    Args:
        arr: List of comparable elements to be sorted (modified in-place)
    
    Returns:
        None (sorts in-place)
    """
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        
        # Move elements of arr[0..i-1] that are greater than key
        # one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert key at its correct position
        arr[j + 1] = key


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    
    insertion_sort(numbers)
    print(f"Sorted array: {numbers}")

