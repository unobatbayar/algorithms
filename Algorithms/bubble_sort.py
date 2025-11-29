"""
Bubble Sort Algorithm

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.
The pass through the list is repeated until the list is sorted.

Time Complexity:
    - Best Case: O(n) - when array is already sorted
    - Average Case: O(n²)
    - Worst Case: O(n²)

Space Complexity: O(1) - in-place sorting

Stable: Yes (maintains relative order of equal elements)
"""


def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.
    
    Args:
        arr: List of comparable elements to be sorted (modified in-place)
    
    Returns:
        None (sorts in-place)
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize: if no swaps occur, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped, array is sorted
        if not swapped:
            break


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    
    bubble_sort(numbers)
    print(f"Sorted array: {numbers}")

