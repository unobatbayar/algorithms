"""
Bucket Sort Algorithm

Bucket Sort divides the range of input values into a number of buckets,
sorts each bucket individually (using another algorithm or recursively),
and then concatenates the sorted buckets.

Time Complexity:
    - Best Case: O(n + k) - when elements are uniformly distributed
    - Average Case: O(n + k)
    - Worst Case: O(n²) - when all elements go to one bucket

Space Complexity: O(n + k)

Stable: Yes (if sorting algorithm used for buckets is stable)

Note: Works best when input is uniformly distributed over a range.
"""


def bucket_sort(arr):
    """
    Sorts an array of floats in range [0.0, 1.0) using Bucket Sort.
    For other ranges, normalize the input first.
    
    Args:
        arr: List of floats in range [0.0, 1.0) to be sorted
    
    Returns:
        Sorted list (does not modify original array)
    """
    if not arr:
        return []
    
    n = len(arr)
    
    # Create n empty buckets
    buckets = [[] for _ in range(n)]
    
    # Put array elements in different buckets
    for num in arr:
        bucket_index = int(n * num)
        buckets[bucket_index].append(num)
    
    # Sort individual buckets (using insertion sort)
    for bucket in buckets:
        insertion_sort(bucket)
    
    # Concatenate all buckets into result
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result


def insertion_sort(arr):
    """
    Helper function: Insertion sort for sorting individual buckets.
    Efficient for small arrays.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Example usage
if __name__ == "__main__":
    # Example with floats in range [0.0, 1.0)
    numbers = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(f"Original array: {numbers}")
    
    sorted_numbers = bucket_sort(numbers)
    print(f"Sorted array: {sorted_numbers}")

