"""
Quick Sort Algorithm

Quick Sort is a divide-and-conquer algorithm that picks a pivot element,
partitions the array around the pivot, and recursively sorts the sub-arrays.

Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n²) - when pivot is always smallest or largest

Space Complexity: O(log n) - average case recursion stack

Stable: No (may change relative order of equal elements)
"""


def quick_sort(arr, low=0, high=None):
    """
    Sorts an array using the Quick Sort algorithm.
    
    Args:
        arr: List of comparable elements to be sorted (modified in-place)
        low: Starting index (default: 0)
        high: Ending index (default: len(arr) - 1)
    
    Returns:
        None (sorts in-place)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition the array and get pivot index
        pivot_idx = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)


def partition(arr, low, high):
    """
    Partitions the array around a pivot element.
    Uses Lomuto partition scheme: last element as pivot.
    
    Args:
        arr: Array to partition
        low: Starting index
        high: Ending index
    
    Returns:
        Final position of pivot element
    """
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element (indicates right position of pivot)
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    
    quick_sort(numbers)
    print(f"Sorted array: {numbers}")

