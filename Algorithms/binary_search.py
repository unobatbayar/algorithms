"""
Binary Search Algorithm

Binary Search is an efficient algorithm for finding an item from a sorted list.
It works by repeatedly dividing in half the portion of the list that could contain
the item, until narrowing down the possible locations to just one.

Time Complexity:
    - Best Case: O(1) - element found at middle
    - Average Case: O(log n)
    - Worst Case: O(log n)

Space Complexity: O(1) - iterative, O(log n) - recursive

Note: Array must be sorted for binary search to work.
"""


def binary_search(arr, target):
    """
    Searches for a target value in a sorted array using Binary Search (iterative).
    
    Args:
        arr: Sorted list of elements to search in
        target: Value to search for
    
    Returns:
        Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Searches for a target value in a sorted array using Binary Search (recursive).
    
    Args:
        arr: Sorted list of elements to search in
        target: Value to search for
        left: Left boundary of search space
        right: Right boundary of search space
    
    Returns:
        Index of target if found, -1 otherwise
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# Example usage
if __name__ == "__main__":
    numbers = [11, 12, 22, 25, 34, 64, 90]  # Must be sorted
    target = 22
    
    result = binary_search(numbers, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")
    
    # Recursive version
    result_rec = binary_search_recursive(numbers, target)
    print(f"Recursive search result: {result_rec}")

