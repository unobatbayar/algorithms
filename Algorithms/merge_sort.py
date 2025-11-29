"""
Merge Sort Algorithm

Merge Sort is a divide-and-conquer algorithm that divides the array into two halves,
recursively sorts each half, and then merges the sorted halves.

Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n log n)

Space Complexity: O(n) - requires additional space for merging

Stable: Yes (maintains relative order of equal elements)
"""


def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm.
    
    Args:
        arr: List of comparable elements to be sorted
    
    Returns:
        Sorted list (does not modify original array)
    """
    if len(arr) <= 1:
        return arr
    
    # Divide: Split array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer: Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    
    Args:
        left: First sorted array
        right: Second sorted array
    
    Returns:
        Merged sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    
    sorted_numbers = merge_sort(numbers)
    print(f"Sorted array: {sorted_numbers}")

