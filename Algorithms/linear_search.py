"""
Linear Search Algorithm

Linear Search sequentially checks each element of the list until a match is found
or the whole list has been searched. It's the simplest search algorithm.

Time Complexity:
    - Best Case: O(1) - element found at first position
    - Average Case: O(n)
    - Worst Case: O(n) - element not found or at last position

Space Complexity: O(1)
"""


def linear_search(arr, target):
    """
    Searches for a target value in an array using Linear Search.
    
    Args:
        arr: List of elements to search in
        target: Value to search for
    
    Returns:
        Index of target if found, -1 otherwise
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    target = 22
    
    result = linear_search(numbers, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")

