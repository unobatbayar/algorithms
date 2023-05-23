def selection_sort(arr):
    """
    Sorts the input array using the selection sort algorithm.
    
    Parameters:
    arr (list): The input list to be sorted.
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Example usage
numbers = [9, 5, 2, 8, 1, 10]
selection_sort(numbers)
print(numbers)
