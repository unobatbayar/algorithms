"""
Counting Sort Algorithm

Counting Sort is a non-comparative integer sorting algorithm.
It counts the number of occurrences of each distinct element,
then uses this information to place elements in their correct positions.

Time Complexity:
    - Best Case: O(n + k) where k is the range of input
    - Average Case: O(n + k)
    - Worst Case: O(n + k)

Space Complexity: O(k) - where k is the range of input

Stable: Yes (maintains relative order of equal elements)

Note: Only works for non-negative integers with a known range.
"""


def counting_sort(arr):
    """
    Sorts an array of non-negative integers using Counting Sort.
    
    Args:
        arr: List of non-negative integers to be sorted
    
    Returns:
        Sorted list (does not modify original array)
    """
    if not arr:
        return []
    
    # Find the maximum value to determine the range
    max_val = max(arr)
    min_val = min(arr)
    
    # Create count array to store count of each element
    count_size = max_val - min_val + 1
    count = [0] * count_size
    
    # Count occurrences of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Modify count array to store cumulative counts
    for i in range(1, count_size):
        count[i] += count[i - 1]
    
    # Build output array
    output = [0] * len(arr)
    
    # Place elements in sorted order (traverse in reverse for stability)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output


# Example usage
if __name__ == "__main__":
    numbers = [4, 2, 2, 8, 3, 3, 1]
    print(f"Original array: {numbers}")
    
    sorted_numbers = counting_sort(numbers)
    print(f"Sorted array: {sorted_numbers}")

