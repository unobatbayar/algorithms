"""
Heap Sort Algorithm

Heap Sort uses a binary heap data structure to sort elements.
It first builds a max heap, then repeatedly extracts the maximum element
and places it at the end of the array.

Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n log n)

Space Complexity: O(1) - in-place sorting

Stable: No (may change relative order of equal elements)
"""


def heap_sort(arr):
    """
    Sorts an array using the Heap Sort algorithm.
    
    Args:
        arr: List of comparable elements to be sorted (modified in-place)
    
    Returns:
        None (sorts in-place)
    """
    n = len(arr)
    
    # Build max heap
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Call heapify on the reduced heap
        heapify(arr, i, 0)


def heapify(arr, n, i):
    """
    Maintains the heap property for a subtree rooted at index i.
    Assumes subtrees are already heapified.
    
    Args:
        arr: Array representing the heap
        n: Size of the heap
        i: Root index of the subtree
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child
    
    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    
    heap_sort(numbers)
    print(f"Sorted array: {numbers}")

