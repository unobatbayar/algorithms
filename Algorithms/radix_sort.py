"""
Radix Sort Algorithm

Radix Sort is a non-comparative integer sorting algorithm that sorts numbers
by processing individual digits. It processes digits from least significant
to most significant, using a stable sorting algorithm (typically counting sort)
as a subroutine.

Time Complexity:
    - Best Case: O(d * (n + k)) where d is number of digits, k is base
    - Average Case: O(d * (n + k))
    - Worst Case: O(d * (n + k))

Space Complexity: O(n + k)

Stable: Yes (maintains relative order of equal elements)

Note: Only works for non-negative integers.
"""


def radix_sort(arr):
    """
    Sorts an array of non-negative integers using Radix Sort.
    
    Args:
        arr: List of non-negative integers to be sorted (modified in-place)
    
    Returns:
        None (sorts in-place)
    """
    if not arr:
        return
    
    # Find the maximum number to know number of digits
    max_val = max(arr)
    
    # Do counting sort for every digit
    # exp is 10^i where i is current digit number
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10


def counting_sort_by_digit(arr, exp):
    """
    Performs counting sort on array according to the digit represented by exp.
    
    Args:
        arr: Array to sort
        exp: Current digit position (1, 10, 100, ...)
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Count array for digits 0-9
    
    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Change count[i] so it contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array (traverse in reverse for stability)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy output array to arr[]
    for i in range(n):
        arr[i] = output[i]


# Example usage
if __name__ == "__main__":
    numbers = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Original array: {numbers}")
    
    radix_sort(numbers)
    print(f"Sorted array: {numbers}")

