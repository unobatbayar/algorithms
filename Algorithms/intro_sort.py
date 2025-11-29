"""
Intro Sort (Introsort) Algorithm

Intro Sort is a hybrid sorting algorithm that combines Quick Sort, Heap Sort,
and Insertion Sort. It starts with Quick Sort, switches to Heap Sort when
the recursion depth exceeds a limit, and uses Insertion Sort for small subarrays.

Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n log n) - guaranteed

Space Complexity: O(log n) - recursion stack

Stable: No (may change relative order of equal elements)
"""


def intro_sort(arr):
    """
    Sorts an array using the Intro Sort algorithm.
    
    Args:
        arr: List of comparable elements to be sorted (modified in-place)
    
    Returns:
        None (sorts in-place)
    """
    max_depth = 2 * (len(arr).bit_length() - 1)
    _intro_sort_recursive(arr, 0, len(arr) - 1, max_depth)


def _intro_sort_recursive(arr, low, high, max_depth):
    """
    Recursive helper function for Intro Sort.
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
        max_depth: Maximum recursion depth before switching to heap sort
    """
    n = high - low + 1
    
    # Use insertion sort for small arrays
    if n <= 16:
        insertion_sort_range(arr, low, high)
        return
    
    # If max depth is 0, use heap sort
    if max_depth == 0:
        heap_sort_range(arr, low, high)
        return
    
    # Otherwise, use quick sort
    pivot = partition(arr, low, high)
    _intro_sort_recursive(arr, low, pivot - 1, max_depth - 1)
    _intro_sort_recursive(arr, pivot + 1, high, max_depth - 1)


def partition(arr, low, high):
    """Partition function for Quick Sort (Lomuto partition scheme)."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def insertion_sort_range(arr, low, high):
    """Insertion sort for a specific range of the array."""
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def heap_sort_range(arr, low, high):
    """Heap sort for a specific range of the array."""
    n = high - low + 1
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_range(arr, low, high, low + i)
    
    # Extract elements from heap
    for i in range(high, low, -1):
        arr[low], arr[i] = arr[i], arr[low]
        heapify_range(arr, low, i - 1, low)


def heapify_range(arr, low, high, i):
    """Heapify for a specific range of the array."""
    largest = i
    left = low + 2 * (i - low) + 1
    right = low + 2 * (i - low) + 2
    
    if left <= high and arr[left] > arr[largest]:
        largest = left
    
    if right <= high and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_range(arr, low, high, largest)


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90, 5, 77, 33, 44, 55, 66]
    print(f"Original array: {numbers}")
    
    intro_sort(numbers)
    print(f"Sorted array: {numbers}")

